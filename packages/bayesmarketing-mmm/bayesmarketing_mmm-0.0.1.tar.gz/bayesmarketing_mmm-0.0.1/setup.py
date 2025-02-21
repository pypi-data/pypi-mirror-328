from setuptools import setup, find_packages

setup(
    name="bayesmarketing_mmm",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "numpyro",
        "jax",
        "jaxlib",
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scipy",
        "arviz"
    ],
    description="Bayesian Marketing Mix Modeling Library using NumPyro",
    long_description=open("README.txt").read(),
    long_description_content_type="text/plain",
    author="Veeramuthu Balakrishnan",
    author_email="v.balak@outlook.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
