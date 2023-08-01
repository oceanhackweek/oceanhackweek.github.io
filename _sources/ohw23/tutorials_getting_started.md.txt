# Getting started on tutorials

## Introduction

Tutorials will be run live on the [OceanHackWeek JupyterHub ("The Hub"), https://oceanhackweek.2i2c.cloud](https://oceanhackweek.2i2c.cloud) in your browser either as Jupyter notebooks or as scripts and notebooks in RStudio. The instructor and all participants can be running their own copies of the tutorial in their Hub account, with files cloned from the OHW source in GitHub.

Below are instructions for getting the tutorials started on the the Hub in your browser, and updating the tutorials files with the latest version from the GitHub tutorials repository, [https://github.com/oceanhackweek/ohw-tutorials](https://github.com/oceanhackweek/ohw-tutorials).

The schedule of tutorials is available [here](../../ohw23/schedule.md), and links to tutorial materials and some background resources will be available there as well.

## How do I get the tutorial repository into the Hub?

For the tutorials, we recommend the use of [nbgitpuller](https://jupyterhub.github.io/nbgitpuller/) to clone and pull the tutorials repository, or update the clone you already have. Use the magical nbgitpuller link below to accomplish this clone or update.

```{admonition} Pull tutorial repo via the magic of nbgitpuller

The nbgitpuller link is magical, but it can't detect which profile you are currently running. Either should update the (same) tutorial repo, but it may error if you use the Python link if you are actively using the R profile, or the other way around.

::::{tab-set}

:::{tab-item} Python

[Pull tutorial repo for the Python profile](https://oceanhackweek.2i2c.cloud/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Foceanhackweek%2Fohw-tutorials&urlpath=lab%2Ftree%2Fohw-tutorials%2F&branch=OHW23)

:::

:::{tab-item} R

[Pull tutorial repo for the R profile](https://oceanhackweek.2i2c.cloud/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Foceanhackweek%2Fohw-tutorials&urlpath=rstudio%2F&branch=OHW23)

:::

::::

```

See this [extended discussion](../resources/prep/jupyterhub.md#how-do-i-get-the-tutorial-repository) for more details about `nbgitpuller` and the alternative approach relying on `git` commands and `GitHub` workflows.
