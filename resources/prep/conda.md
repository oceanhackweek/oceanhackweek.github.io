# Conda

_or: How I Learned to Stop Worrying and Manage Python and R_

The JupyterHub offers pre-configured environments -- for Python and for R -- that are designed to be able to run all the tutorial notebooks, and support a broad range of oceanographic applications.

This environment is created and managed using the open-source [**Conda** package and environment management system](https://docs.conda.io) for installing multiple versions of software packages together with their dependencies, and convenient switching between environments. 

## What is Conda?
[**Conda**](http://conda.pydata.org/docs/) is an **open source `package` and `environment` management system for any programming languages, but very popular among the Python community,**

Conda runs on Windows, macOS, and Linux: *"Conda quickly installs, runs, and updates packages and their dependencies. Conda easily creates, saves, loads, and switches between environments on your local computer. It was created for Python programs but it can package and distribute software for any language."*

For Python, the advantage of conda compared to `pip` is that it has a built in environment management system as well as the management of binaries, and non-Python dependencies.

## Conda on the JupyterHub

The JupyterHub has both a pre-configured base environment, and environments that you create and manage yourself.

### JupyterHub base environment

You pick the base environment when you start your server, from the **Environment** dropdown on CryoCloud's Server Options page -- see [How do I access the shared cloud environment?](jupyterhub.md#how-do-i-access-the-shared-cloud-environment) for a walkthrough. The OceanHackWeek image contains hopefully everything you will need for the tutorials and for general exploration.

The base environment also contains a lot of supporting infrastructure for running each individual's JupyterLab server, so if you need something different we suggest building up your own environment from scratch, rather than by trimming down the base environment.

### Temporary packages

You can temporarily add packages to your hub, via Jupyter cell magic, `%pip install <list-of-packages>` or `%conda install <list-of-packages>`. [Jupyter magics](https://ipython.readthedocs.io/en/stable/interactive/magics.html) always start with the character `%`. In R you can use `install.packages("package-name")` as usual.

:::{admonition} pip install trouble
:class: danger

For those who know their way around Jupyter, you may be tempted to `!pip install <list-of-packages>`. This can leave your environment in an inconsistent state, which may prevent your server from starting (and will require some heavy duty assistance from `@help-infrastructure` to debug). More information is [available here.](https://docs.2i2c.org/user/get-started/)

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

Conda may be used on your computer as well as the Hub, and we encourage you to practice with it locally so that you can keep working after the event. If a tutorial ships an `environment.yml` alongside its notebooks in [`oceanhackweek/ohw-tutorials`](https://github.com/oceanhackweek/ohw-tutorials), you can recreate that environment locally with `conda env create -n <ENV NAME> --file environment.yml`.

### Installing Conda

There are a few different ways to install conda:

- The [Anaconda Individual Edition](https://www.anaconda.com/products/individual) which comes with a large pre-packaged environment, and a snazzy management interface to help explore what packages are available and what environments you have installed.
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a stripped down version with just the installer, which is really for kick starting other environments.
- There is also [Mamba](https://mamba.readthedocs.io/en/latest/index.html) which is a newer take on Conda that tends to be faster, but isn't currently compatible with our trick to allow you to set up your own Conda environments ([nb_conda_kernels](https://github.com/Anaconda-Platform/nb_conda_kernels)).

We recommend the use of Miniconda.
