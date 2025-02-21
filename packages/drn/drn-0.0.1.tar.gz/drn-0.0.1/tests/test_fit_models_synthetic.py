import os

# os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"

import numpy as np
import pandas as pd
import torch
import statsmodels.api as sm
from statsmodels.genmod.families import Gamma
from synthetic_dataset import generate_synthetic_data

from drn import *


def check_crps(model, X_train, Y_train, grid_size=3000):
    grid = torch.linspace(0, Y_train.max().item() * 1.1, grid_size).unsqueeze(-1)
    grid = grid.to(X_train.device)
    dists = model.distributions(X_train)
    cdfs = dists.cdf(grid)
    grid = grid.squeeze()
    crps_ = crps(Y_train, grid, cdfs)
    assert crps_.shape == Y_train.shape
    assert crps_.mean() > 0


def test_glm():
    print("\n\nTraining GLM\n")
    X_train, Y_train, train_dataset, val_dataset = generate_synthetic_data()

    torch.manual_seed(1)
    glm = GLM(X_train.shape[1], distribution="gamma")

    train(
        glm,
        gamma_deviance_loss,
        train_dataset,
        val_dataset,
        epochs=2,
    )

    glm.update_dispersion(X_train, Y_train)

    check_crps(glm, X_train, Y_train)


def test_glm_from_statsmodels():
    print("\n\nTraining GLM\n")
    X_train, Y_train, train_dataset, val_dataset = generate_synthetic_data()

    # Construct GLM given training data in torch tensors
    glm = GLM.from_statsmodels(X_train, Y_train, distribution="gamma")

    our_dispersion = gamma_estimate_dispersion(
        glm.forward(X_train), Y_train, X_train.shape[1]
    )

    assert np.isclose(our_dispersion, glm.dispersion.item())

    # Construct GLM given training data in numpy arrays
    glm = GLM.from_statsmodels(
        X_train.detach().cpu().numpy(),
        Y_train.detach().cpu().numpy(),
        distribution="gamma",
    )
    glm = glm.to(
        X_train.device
    )  # since 'from_statsmodels' didn't know this information
    our_dispersion = gamma_estimate_dispersion(
        glm.forward(X_train), Y_train, X_train.shape[1]
    )

    assert np.isclose(our_dispersion, glm.dispersion.item())

    # Check we avoid this 'iloc' warning when training on pandas data types
    X_df = pd.DataFrame(
        X_train.detach().cpu().numpy(),
        columns=[f"X_{i}" for i in range(X_train.shape[1])],
    )
    y_ser = pd.Series(Y_train.detach().cpu().numpy(), name="Y")
    glm = GLM.from_statsmodels(X_df, y_ser, distribution="gaussian")

    # Check that pandas objects from split_and_preprocess
    (
        x_train,
        x_val,
        x_test,
        y_train,
        y_val,
        y_test,
        x_train_raw,
        x_val_raw,
        x_test_raw,
        num_features,
        cat_features,
        all_categories,
        ct,
    ) = split_and_preprocess(
        X_df, y_ser, ["X_0", "X_1", "X_2", "X_3"], [], seed=42, num_standard=True
    )

    glm = GLM.from_statsmodels(x_train, y_train, distribution="gamma")
    glm = glm.to(X_train.device)

    # Check that statsmodels predictions are just the same as ours
    # Choose the correct family based on the distribution
    model = sm.GLM(
        y_train, sm.add_constant(x_train), family=Gamma(link=sm.families.links.Log())
    )
    results = model.fit()
    statsmodels_predictions = results.predict(sm.add_constant(x_train))

    X_train = torch.tensor(x_train.values, dtype=X_train.dtype, device=X_train.device)
    our_predictions = glm.forward(X_train).detach().cpu().numpy()

    assert np.allclose(statsmodels_predictions, our_predictions)


def test_cann():
    print("\n\nTraining CANN\n")
    X_train, Y_train, train_dataset, val_dataset = generate_synthetic_data()

    torch.manual_seed(2)
    glm = GLM(X_train.shape[1], distribution="gamma")
    train(
        glm,
        gamma_deviance_loss,
        train_dataset,
        val_dataset,
        epochs=2,
    )

    cann = CANN(glm, num_hidden_layers=2, hidden_size=100)
    train(
        cann,
        gamma_deviance_loss,
        train_dataset,
        val_dataset,
        epochs=2,
    )

    cann.update_dispersion(X_train, Y_train)

    check_crps(cann, X_train, Y_train)


def test_mdn():
    print("\n\nTraining MDN\n")
    X_train, Y_train, train_dataset, val_dataset = generate_synthetic_data()

    torch.manual_seed(3)
    mdn = MDN(X_train.shape[1], num_components=5, distribution="gamma")
    train(
        mdn,
        gamma_mdn_loss,
        train_dataset,
        val_dataset,
        epochs=2,
    )

    check_crps(mdn, X_train, Y_train)


def setup_cutpoints(Y_train):
    max_y = torch.max(Y_train).item()
    len_y = torch.numel(Y_train)
    c_0 = 0.0
    c_K = max_y * 1.01
    p = 0.1
    num_cutpoints = int(np.ceil(p * len_y))
    cutpoints_ddr = list(np.linspace(c_0, c_K, num_cutpoints))
    assert len(cutpoints_ddr) >= 2
    return cutpoints_ddr


def test_ddr():
    print("\n\nTraining DDR\n")
    X_train, Y_train, train_dataset, val_dataset = generate_synthetic_data()

    cutpoints_ddr = setup_cutpoints(Y_train)

    torch.manual_seed(4)
    ddr = DDR(X_train.shape[1], cutpoints_ddr, hidden_size=100)
    train(ddr, ddr_loss, train_dataset, val_dataset, epochs=2)

    check_crps(ddr, X_train, Y_train)


def test_drn():
    print("\n\nTraining DRN\n")
    X_train, Y_train, train_dataset, val_dataset = generate_synthetic_data()
    y_train = Y_train.cpu().numpy()

    cutpoints_ddr = setup_cutpoints(Y_train)
    cutpoints_drn = merge_cutpoints(cutpoints_ddr, y_train, min_obs=2)
    assert len(cutpoints_drn) >= 2

    torch.manual_seed(5)
    glm = GLM(X_train.shape[1], distribution="gamma")
    train(
        glm,
        gamma_deviance_loss,
        train_dataset,
        val_dataset,
        epochs=2,
    )
    glm.update_dispersion(X_train, Y_train)

    drn = DRN(X_train.shape[1], cutpoints_drn, glm, hidden_size=100)

    # Try both loss functions with their regularisation terms enabled
    train(
        drn,
        lambda pred, y: drn_loss(
            pred, y, kind="jbce", kl_alpha=1, mean_alpha=1, dv_alpha=1, tv_alpha=1
        ),
        train_dataset,
        val_dataset,
        epochs=2,
    )
    train(
        drn,
        lambda pred, y: drn_loss(
            pred, y, kind="nll", kl_alpha=1, mean_alpha=1, dv_alpha=1, tv_alpha=1
        ),
        train_dataset,
        val_dataset,
        epochs=2,
    )

    check_crps(drn, X_train, Y_train)


def test_torch():
    X_train, Y_train, train_dataset, val_dataset = generate_synthetic_data()

    cutpoints = setup_cutpoints(Y_train)

    torch.manual_seed(5)
    glm = GLM.from_statsmodels(X_train, Y_train, distribution="gamma")

    hs = 5
    drn = DRN(X_train.shape[1], cutpoints, glm, num_hidden_layers=2, hidden_size=hs)
    train(
        drn,
        drn_loss,
        train_dataset,
        val_dataset,
        epochs=2,
    )

    # Calculate the expected number of weights & biases given two layers of hs hidden units
    expected_num_weights = hs * X_train.shape[1] + hs + hs * hs + hs
    num_weights = sum([p.numel() for p in drn.hidden_layers.parameters()])
    assert num_weights == expected_num_weights

    # Try again using np.int64 instead of ints for the hyperparameters
    drn = DRN(
        X_train.shape[1],
        cutpoints,
        glm,
        num_hidden_layers=np.int64(2),
        hidden_size=np.int64(hs),
    )
    num_weights = sum([p.numel() for p in drn.hidden_layers.parameters()])
    assert num_weights == expected_num_weights and len(drn.hidden_layers) // 3 == 2

    train(
        drn,
        drn_loss,
        train_dataset,
        val_dataset,
        epochs=2,
    )

    # Check dropout is working as intended
    drn = DRN(
        X_train.shape[1],
        cutpoints,
        glm,
        num_hidden_layers=2,
        hidden_size=hs,
        dropout_rate=0.5,
    )
    train(
        drn,
        drn_loss,
        train_dataset,
        val_dataset,
        epochs=2,
    )

    # Make sure two different predictions (which in drn.train mode) are different
    drn.train()
    preds1 = drn(X_train)[-1]
    preds2 = drn(X_train)[-1]
    assert not torch.allclose(preds1, preds2)

    # Make sure two different predictions (which in drn.eval mode) are the same
    drn.eval()
    preds1 = drn(X_train)[-1]
    preds2 = drn(X_train)[-1]
    assert torch.allclose(preds1, preds2)
