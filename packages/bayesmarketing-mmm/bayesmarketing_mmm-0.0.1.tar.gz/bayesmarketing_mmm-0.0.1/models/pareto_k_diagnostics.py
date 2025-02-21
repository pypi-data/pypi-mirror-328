import arviz as az
import numpyro
import numpyro.distributions as dist
import jax.numpy as jnp
import pandas as pd
from numpyro.infer import MCMC, NUTS

def bayesian_model_for_loo(data):
    """
    A simple Bayesian model for demonstrating LOO-CV and Pareto k diagnostics.
    """
    intercept = numpyro.sample("intercept", dist.Normal(0, 1))
    beta = numpyro.sample("beta", dist.Normal(0, 1))
    sigma = numpyro.sample("sigma", dist.Exponential(1.0))

    mu = intercept + beta * data["x"].values
    numpyro.sample("obs", dist.Normal(mu, sigma), obs=data["y"].values)

def run_pareto_k_example():
    """
    Example usage of LOO-CV and Pareto k diagnostics.
    """
    data = pd.DataFrame({
        "x": jnp.linspace(0, 10, 20),
        "y": jnp.linspace(5, 15, 20) + jnp.random.normal(0, 2, 20)
    })

    nuts_kernel = NUTS(bayesian_model_for_loo)
    mcmc = MCMC(nuts_kernel, num_warmup=500, num_samples=2000, num_chains=1)
    mcmc.run(random.PRNGKey(0), data)

    posterior_samples = mcmc.get_samples()
    loo = az.loo(posterior_samples)
    print("LOO-CV:", loo)
    print("Pareto k diagnostics:", loo.pareto_k)
