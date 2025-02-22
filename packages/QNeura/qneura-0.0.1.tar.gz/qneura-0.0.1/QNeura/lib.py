# jax
try:
    import jax
    JAX_AVAILABLE = True
except ImportError:
    JAX_AVAILABLE = False

# flax
try:
    import flax
    FLAX_AVAILABLE = True
except ImportError:
    FLAX_AVAILABLE = False

