import numpy as np
import torch
import torch.nn as nn

from ..distributions.histogram import Histogram


class DDR(nn.Module):
    def __init__(
        self, p: int, cutpoints, num_hidden_layers=2, hidden_size=100, dropout_rate=0.2
    ):
        """
        Args:
            x_train_shape: The shape of the training data, used to define the input size of the first layer.
            cutpoints: The cutpoints for the DDR model.
            num_hidden_layers: The number of hidden layers in the network.
            hidden_size: The number of neurons in each hidden layer.
        """
        super(DDR, self).__init__()
        self.cutpoints = nn.Parameter(torch.Tensor(cutpoints), requires_grad=False)
        self.p = p

        layers = [
            nn.Linear(self.p, hidden_size),
            nn.LeakyReLU(),
            nn.Dropout(dropout_rate),
        ]
        for _ in range(num_hidden_layers - 1):
            layers.append(nn.Linear(hidden_size, hidden_size))
            layers.append(nn.LeakyReLU())
            layers.append(nn.Dropout(dropout_rate))

        # Use nn.Sequential to chain the layers together
        self.hidden_layers = nn.Sequential(*layers)

        # Output layer for the pi values
        self.pi = nn.Linear(hidden_size, len(self.cutpoints) - 1)

    def forward(self, x):
        """
        Forward pass of the DDR model.
        Args:
            x: Input tensor.
        Returns:
            The cutpoints and probabilities for the DDR model.
        """
        # Pass input through the dynamically created hidden layers
        h = self.hidden_layers(x)

        # Calculate probabilities using the final layer
        probs = torch.softmax(self.pi(h), dim=1)

        return self.cutpoints, probs

    def distributions(self, x):
        cutpoints, prob_masses = self.forward(x)
        dists = Histogram(cutpoints, prob_masses)
        assert dists.batch_shape == torch.Size([x.shape[0]])
        return dists


def jbce_loss(dists, y, alpha=0.0):
    """
    The joint binary cross entropy loss.
    Args:
        dists: the predicted distributions
        y: the observed values
        alpha: the penalty parameter
    """

    cutpoints = dists.cutpoints
    cdf_at_cutpoints = dists.cdf_at_cutpoints()

    assert cdf_at_cutpoints.shape == torch.Size([len(cutpoints), len(y)])

    n = y.shape[0]
    C = len(cutpoints)

    # The cross entropy loss can't accept 0s or 1s for the cumulative probabilities.
    epsilon = 1e-15
    cdf_at_cutpoints = cdf_at_cutpoints.clamp(epsilon, 1 - epsilon)

    # Change: C to C-1
    losses = torch.zeros(C - 1, n, device=y.device, dtype=y.dtype)

    for i in range(1, C):
        targets = (y <= cutpoints[i]).float()
        probs = cdf_at_cutpoints[i, :]
        losses[i - 1, :] = nn.functional.binary_cross_entropy(
            probs, targets, reduction="none"
        )

    return torch.mean(losses)


def ddr_loss(pred, y, alpha=0.0):
    cutpoints, prob_masses = pred
    dists = Histogram(cutpoints, prob_masses)
    return jbce_loss(dists, y, alpha)


def nll_loss(dists, y, alpha=0.0):
    losses = -(dists.log_prob(y))
    return torch.mean(losses)


def ddr_cutpoints(c_0, c_K, p, y):
    num_cutpoints = int(np.ceil(p * len(y)))
    cutpoints = list(np.linspace(c_0, c_K, num_cutpoints))

    return cutpoints
