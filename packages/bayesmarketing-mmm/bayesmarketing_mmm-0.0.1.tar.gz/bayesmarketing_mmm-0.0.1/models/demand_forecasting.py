import numpyro
import numpyro.distributions as dist
from numpyro.contrib.gp.kernels import RBF
from numpyro.contrib.gp.model import GPRegression
from numpyro.infer import MCMC, NUTS
import jax.numpy as jnp
import pandas as pd
from jax import random

def bayesian_demand_forecast(time, sales):
    """
    Bayesian Demand Forecasting using Gaussian Processes.
    """
    kernel = RBF()
    gpr = GPRegression(time, sales, kernel, noise=dist.Exponential(1.0))

    gpr_log_likelihood = gpr.marginal_log_likelihood()
    numpyro.sample("obs", gpr_log_likelihood, obs=sales)

def run_forecasting_example():
    """
    Example usage of Bayesian Demand Forecasting.
    """
    data = pd.DataFrame({
        "time": jnp.arange(1, 11),
        "sales": jnp.array([100, 120, 130, 150, 170, 190, 200, 230, 250, 270])
    })

    time = data["time"].values
    sales = data["sales"].values

    nuts_kernel = NUTS(bayesian_demand_forecast)
    mcmc = MCMC(nuts_kernel, num_warmup=500, num_samples=2000, num_chains=1)
    mcmc.run(random.PRNGKey(0), time, sales)
    print(mcmc.get_samples())
