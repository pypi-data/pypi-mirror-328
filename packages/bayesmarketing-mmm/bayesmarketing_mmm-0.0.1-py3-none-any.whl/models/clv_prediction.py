import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS
import jax.numpy as jnp
import pandas as pd
from jax import random

def bayesian_clv_model(frequency, monetary_value):
    """
    Bayesian Customer Lifetime Value (CLV) Model using Gamma-Gamma Distribution.
    """
    alpha = numpyro.sample("alpha", dist.Gamma(2.0, 1.0))
    beta = numpyro.sample("beta", dist.Gamma(2.0, 1.0))
    sigma = numpyro.sample("sigma", dist.Exponential(1.0))

    mu = alpha * frequency / (beta + frequency)
    numpyro.sample("obs", dist.Normal(mu * monetary_value, sigma), obs=monetary_value)

def run_clv_example():
    """
    Example usage of the Bayesian CLV model.
    """
    data = pd.DataFrame({
        "frequency": [1, 3, 5, 7, 9],
        "monetary_value": [10, 25, 40, 55, 70]
    })

    frequency = data["frequency"].values
    monetary_value = data["monetary_value"].values

    nuts_kernel = NUTS(bayesian_clv_model)
    mcmc = MCMC(nuts_kernel, num_warmup=500, num_samples=2000, num_chains=1)
    mcmc.run(random.PRNGKey(0), frequency, monetary_value)
    print(mcmc.get_samples())
