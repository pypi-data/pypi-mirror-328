import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS
import jax.numpy as jnp
import pandas as pd
from jax import random

def bayesian_ucm_model(time, sales):
    """
    Bayesian Unobserved Components Model (UCM) for Trend Analysis.
    """
    trend = numpyro.sample("trend", dist.Normal(0, 1), sample_shape=(len(time),))
    seasonal = numpyro.sample("seasonal", dist.Normal(0, 1), sample_shape=(len(time),))
    sigma = numpyro.sample("sigma", dist.Exponential(1.0))

    mu = trend + seasonal
    numpyro.sample("obs", dist.Normal(mu, sigma), obs=sales)

def run_ucm_example():
    """
    Example usage of Bayesian Unobserved Components Model.
    """
    data = pd.DataFrame({
        "time": jnp.arange(1, 25),
        "sales": jnp.array([100, 120, 140, 180, 220, 260, 300, 340, 280, 250, 230, 190] * 2)
    })

    time = data["time"].values
    sales = data["sales"].values

    nuts_kernel = NUTS(bayesian_ucm_model)
    mcmc = MCMC(nuts_kernel, num_warmup=500, num_samples=2000, num_chains=1)
    mcmc.run(random.PRNGKey(0), time, sales)
    print(mcmc.get_samples())
