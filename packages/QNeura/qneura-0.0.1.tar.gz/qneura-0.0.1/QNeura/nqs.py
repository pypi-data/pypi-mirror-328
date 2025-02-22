
#
# Author: Yu Zhang <zhy@lanl.gov>
#

r"""
Neural network quantum states
-----------------------------



"""
from typing import Any, Callable, Sequence
import jax
import jax.numpy as jnp
from flax import linen as nn


class ConvNN(nn.Module):
    """
    A simple multi-layer Convolutional Neural Network in Flax.

    Args:
        channels (Sequence[int]): Number of output channels for each conv layer.
        kernel_sizes (Sequence): Kernel sizes for each conv layer.
        activation (Any): Activation function (default: nn.relu).
        kernel_init (Any): Kernel initializer (default: lecun_normal).
        bias_init (Any): Bias initializer (default: zeros).
        param_dtype (Any): Data type for parameters (default: float32).
    """
    channels: Sequence[int]
    kernel_sizes: Sequence
    activation: Any = nn.relu
    kernel_init: Any = jax.nn.initializers.lecun_normal()
    bias_init: Any = jax.nn.initializers.zeros
    param_dtype: Any = jnp.float32

    @nn.compact
    def __call__(self, x: jnp.ndarray) -> jnp.ndarray:
        # Reshape input to include a batch dimension (if needed)
        x = x.reshape((1, *x.shape))

        # Apply each conv layer with corresponding channels and kernel size
        for c, k in zip(self.channels, self.kernel_sizes):
            x = nn.Conv(
                features=c,
                kernel_size=k,
                padding="CIRCULAR",  # Adjust padding as needed
                param_dtype=self.param_dtype,
                kernel_init=self.kernel_init,
                bias_init=self.bias_init,
            )(x)
            # Apply chosen activation
            x = self.activation(x)

        # Return the sum of all elements in x as a single-element array
        return jnp.array([jnp.sum(x)])

##
class NQSBase(object):
    r"""
    Base neural network quantum states
    # TBA.
    """
    def __init__(self, *args, **kwargs):
        pass


# Jastrow NQS
class nn_jastrow(NQSBase):
    r"""Jastrow type NN wavefunction

    """
    def __init__(
        self,
        nn_apply: Callable,
        reference: Any,
        n_parameters: int,
        **kwargs,
    ):
        self.nn_apply = nn_apply
        self.reference = reference
        self.n_parameters = n_parameters
        # get_input is callable function
        self.get_input = kwargs.get("get_input",  get_input_k)


    def get_ovlap(self, walkers):
        r"""Compute overlap

        """
        pass







# =================================
# examples
# =================================


def cnn_sample():
    input_data = jnp.ones((28, 28))

    # 2) Instantiate the model
    model = ConvNN(
        channels=[8, 16],          # Two conv layers, first has 8 filters, second has 16
        kernel_sizes=[(3, 3), (3, 3)]  # Both conv layers use a 3x3 kernel
    )

    # 3) Initialize parameters
    key = jax.random.PRNGKey(0)
    variables = model.init(key, input_data)
    # 'variables' now contains {'params': {...}} with randomly initialized weights

    # 4) Apply the model to the input
    output = model.apply(variables, input_data)

    print("Output shape:", output.shape)
    print("Output value:", output)


if __name__ == "__main__":
    cnn_sample()
