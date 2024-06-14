# Conda

_or: How I Learned to Stop Worrying and Manage Python and R_

The JupyterHub is pre-configured with customized environments for both Python and R packages that are designed to be able to run all the tutorial notebooks, and support a broad range of oceanographic applications.

This environment is created and managed using the open-source [**Conda** package and environment management system](https://docs.conda.io) for installing multiple versions of software packages together with their dependencies, and convenient switching between environments. 

## What is Conda?
[**Conda**](http://conda.pydata.org/docs/) is an **open source `package` and `environment` management system for any programming languages, but very popular among the Python community,**

Conda runs on Windows, macOS, and Linux: *"Conda quickly installs, runs, and updates packages and their dependencies. Conda easily creates, saves, loads, and switches between environments on your local computer. It was created for Python programs but it can package and distribute software for any language."*

For Python, the advantage of conda compared to `pip` is that it has a built in environment management system as well as the management of binaries, and non-Python dependencies.

## Conda on the JupyterHub

The JupyterHub has both a pre-configured base environment, and environments that you create and manage yourself.

### JupyterHub base environment

The Conda environment for the base JupyterHub environments are defined in [oceanhackweek/jupyter-image](https://github.com/oceanhackweek/jupyter-image/). These image contains hopefully everything you will need for the tutorials and for general exploration.

The `environment.yml` files ([Python](https://github.com/oceanhackweek/jupyter-image/blob/main/py-base/environment.yml), [R](https://github.com/oceanhackweek/jupyter-image/blob/main/r/environment.yml)) captures the current state of the OceanHackWeek environment. You can explore these files to see what packages we have selected to come in the base environment.

```yaml
# environment.yml
name: OHW
channels:
  - conda-forge
dependencies:
  - python=3.9
  - pangeo-notebook=2021.07.24
  - argopy
  - bokeh
  - bottleneck
  - cartopy
  - cdsapi
  - cf-units
  - cf_xarray
  - cmip6_preprocessing
  - cmocean
  - colorcet
  - compilers
  - compliance-checker
  - conda-lock
#   ... oh so many more packages that we are not going to include them all here
```

It also contains a lot of supporting infrastructure for running each individual's JupyterLab server (for instance `compilers` and `conda-lock` in just that small subset), so we suggest building up an environment from scratch, rather than by trimming down the base environment.

The exact state of the Conda environments are captured in `conda-linux-64.lock` in the same directories that includes the exact versions of all the packages, not just the ones we selected.

There are also a handful of dependencies that are installed directly in the `Dockerfiles` that are also in the same directories.

The full environments are captured as [Docker images](https://github.com/orgs/oceanhackweek/packages?repo_name=jupyter-image) that can be pulled and run locally.

### Temporary packages

You can temporarily add packages to your hub, via Jupyter cell magic, `%pip install <list-of-packages>` or `%conda install <list-of-packages>`. [Jupyter magics](https://ipython.readthedocs.io/en/stable/interactive/magics.html) always start with the character `%`. In R you can use `install.packages("package-name")` as usual.

:::{admonition} pip install trouble
:class: danger

For those who know their way around Jupyter, you may be tempted to `!pip install <list-of-packages>`. This can leave your environment in an inconsistent state, which may prevent your server from starting (and will require some heavy duty assistance from `@help-infrastructure` to debug). More information is [available here.](https://docs.2i2c.org/en/latest/admin/howto/environment/index.html#temporarily-install-packages-for-a-session)

:::

### Create your own environment on JupyterHub

To create your own Conda environment on JupyterHub, you can launch the terminal and run `conda create` commands as expected. Be sure to specify `-n <environment-name>`. For a Python environment:

`conda create -n cool-project -c conda-forge python=3.9 xarray ipykernel`

:::{admonition} Kernel needed
:class: warning

In order to get easy notebook or terminal access in JupyterLab, a Jupyter kernel needs to be included in the environment, such as `ipykernel` for Python or `irkernel` for R.

:::

Once you've created an environment, you can run `conda activate cool-project` as usual for access to the environment in the terminal.

To use the kernel in a notebook, it has to be installed or registered.
The specifics process will vary by kernel, but in general it will need to happen from within the activated environment.

For Python it often looks like `python -m ipykernel install --user --name <name-to-display-in-jupyterhub>`.

:::{admonition} Wait for it...

It may take a minute or two for JupyterLab to show your new Conda environment.
The [package](https://github.com/Anaconda-Platform/nb_conda_kernels) that detects additional environments doesn't run constantly, so give it a second before worrying that you created an environment wrong.

:::

## Conda on your own computer

Conda may be used on your computer as well as the Hub. If you wish to install the same environment as the hub is running, after you install Conda, you can download the [`environment.yml`](https://raw.githubusercontent.com/oceanhackweek/ohw-tutorials/d51c880111305d7e345d98b7d8ccc031cbf0087e/environment.yml) that we use, then `conda env create -n <ENV NAME> --file environment.yml`

### Installing Conda

There are a few different ways to install conda:

- The [Anaconda Individual Edition](https://www.anaconda.com/products/individual) which comes with a large pre-packaged environment, and a snazzy management interface to help explore what packages are available and what environments you have installed.
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a stripped down version with just the installer, which is really for kick starting other environments. We're using a Miniconda Docker image.
- There is also [Mamba](https://mamba.readthedocs.io/en/latest/index.html) which is a newer take on Conda that tends to be faster, but isn't currently compatible with our trick to allow you to set up your own Conda environments ([nb_conda_kernels](https://github.com/Anaconda-Platform/nb_conda_kernels)).

We recommend the use of Miniconda.
