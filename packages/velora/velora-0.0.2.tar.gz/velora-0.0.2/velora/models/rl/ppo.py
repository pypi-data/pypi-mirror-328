from velora.models import LiquidNCPNetwork

import torch
import torch.nn as nn


class LiquidPPO(nn.Module):
    """
    A Liquid Network variant of the Proximal Policy Optimization (PPO)
    algorithm.

    Parameters:
        in_features (int): number of inputs (sensory nodes)
        n_neurons (int): number of decision nodes (inter and command nodes).
            Nodes are set automatically based on the following:
            ```python
            command_neurons = max(int(0.4 * n_neurons), 1)
            inter_neurons = n_neurons - command_neurons
            ```
        out_features (int): number of out features (motor nodes)
        sparsity_level (float, optional): controls the connection sparsity
            between neurons. Must be a value between `[0.1, 0.9]`. When `0.1` neurons are very dense, when `0.9` they are very sparse. Default
            is '0.5'
        device (torch.device, optional): the device to load `torch.Tensors` onto.
            Default is 'None'
    """

    def __init__(
        self,
        in_features: int,
        n_neurons: int,
        out_features: int,
        *,
        sparsity_level: float = 0.5,
        device: torch.device | None = None,
    ) -> None:
        super().__init__()

        self.in_features = in_features
        self.n_neurons = n_neurons
        self.out_features = out_features

        self.actor = LiquidNCPNetwork(
            in_features,
            n_neurons,
            out_features,
            sparsity_level=sparsity_level,
            device=device,
        ).to(device)
        self.critic = LiquidNCPNetwork(
            in_features,
            n_neurons,
            out_features,
            sparsity_level=sparsity_level,
            device=device,
        ).to(device)
