# Python Requirements

## Overview

Python software is distributed as a series of *libraries* that are called within your code to perform certain tasks. There are many different collections, or *distributions* of Python software. Generally you install a specific distribution of Python and then add additional libraries as you need them. There are also several different *versions* of Python. The two main versions right now are 2.7 and 3.7. During the hackweek we will be using Python 3.7 for the tutorials, and encouraging participants to do so. If you have only used Python 2 in the past check out the key differences [here](https://www.geeksforgeeks.org/important-differences-between-python-2-x-and-python-3-x-with-examples/).

Even though Python is one of the most adaptable, easy-to-use software systems, you can see there are still complexities to work out and potential challenges when delivering content to a large group. Therefore we have a number of different ways that we are trying to simplify this process to maximize your learning during Oceanhackweek.

We will be using Ocean [Pangeo](https://pangeo.io/) ([http://ocean.pangeo.io](http://ocean.pangeo.io)), which is a platform for using Jupyter Notebooks in the ocean, atmospheric, and climate research community.
A [Jupyter Notebook](https://jupyter.org/) is an open-source web application that allows users to create and share documents containing live code, equations, visualizations, and markdown texts.

## Setting up Python locally

Although, you we will provide you with a Python working environment, it will be good if you set up Python locally on your laptop: you might need it for some of your project work, Python review, or for future Python development. We recommend installing the [Miniconda](https://conda.io/miniconda.html) Python distribution. We can assist in setting up "conda" environments that will simplify the gathering of Python libraries and version specific to the tutorial you are working on.

[**Conda**](http://conda.pydata.org/docs/) is an **open source `package` and `environment` management system for python libraries**. We will be using various
Python libraries with multiple dependencies, so it is critical that you have some sort of 
package management system in place. Conda can be installed in almost any computer. The advantage of [`conda` compared to `pip`](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions) is that it has a built in environment management system as well as the management of binaries, and non-python dependencies.

Here are the system requirements:

- 32-bit or 64-bit computer.
- Minimum 400 MB disk space to download and install.
- Windows Vista or newer, OS X 10.7+, or Linux (Ubuntu, RedHat and others; CentOS 5+)

*NOTE: You do not need administrative or root permissions to install conda if you select a user-writable install location.*

To test your installation you can run `python` in the terminal and check if the version you have is Miniconda Python 3. Let us know if on Slack you are having problems with installing Conda.


## Brushing up on Python

Given all the heavy use of Python during Oceanhackweek, we will not be able to provide instruction in Python fundamentals. We expect you to have basic Python familiarity on the level of manipulating variables (lists, arrays), writing loops/functions, making simple plots. If you have not used Python before or it has been a while since you have used it, please, go thouroughly through the lesson below

* [Software Carpentry Python Tutorial](https://swcarpentry.github.io/python-novice-gapminder/) (1 day workshop with exercises)
* [Notebook environment](https://mybinder.org/v2/gh/swcarpentry/python-novice-gapminder/binder)

The more, the better! Here are a few more Python resources:
* [Codecademy Lesson](https://www.codecademy.com/learn/learn-python-3) (25 hours)
* [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) (on your own pace)
