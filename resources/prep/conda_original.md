# Conda and installing Python and R environments

### Overview 

### What is Conda?
[**Conda**](http://conda.pydata.org/docs/) is an **open source `package` and `environment` management system for any programming languages, but very popular among python community,**

The Hub is pre-configured with a customized "environment" of Python and R packages designed to run all the tutorial notebooks, and supporting a broad range of oceanographic applications. This environment is created and managed using the open-source [**Conda** package and environment management system](https://docs.conda.io) for installing multiple versions of software packages together with their dependencies, and convenient switching between environments. Conda runs on Windows, macOS, and Linux: *"Conda quickly installs, runs, and updates packages and their dependencies. Conda easily creates, saves, loads, and switches between environments on your local computer. It was created for Python programs but it can package and distribute software for any language."*

Conda may be used on your computer as well as the Hub ...

https://github.com/oceanhackweek/ohw20-tutorials/blob/master/environment.yml

For Python, the advantage of conda compared to `pip` is that it has a built in environment management system as well as the management of binaries, and non-Python dependencies.

You do not need administrative or root permissions to install conda if you select a user-writable installation location.


In the previous lesson we showed you a cloud-based environment for our work during the hackweek. What happens after the event when you want to go home and work with all the libraries we showed you? You will likely also want to have a functioning version of Python on your local laptop if that is not already in place. So this lesson takes you through our recommended procedure for doing that. We suggest you get this set up in advance so that we can help you troubleshoot when you arrive.

### Python Software

Python software is distributed as a series of *libraries* that are called within your code to perform certain tasks. There are many different collections, or *distributions* of Python software. Generally you install a specific distribution of Python and then add additional libraries as you need them. There are also several different *versions* of Python. The two main versions right now are 2.7 and 3.7, although Python 2.7 will not be supported past 2020. Some libraries only work with specific versions of Python.

So even though Python is one of the most adaptable, easy-to-use software systems, you can see there are still complexities to work out and potential challenges when delivering content to a large group. Therefore we have a number of different ways that we are trying to simplify this process to maximize your learning during the hackweek.

We also provide instructions for using [Anaconda](https://www.continuum.io), which is our recommended Python distribution, for installing and working with Python on your local computer. We can assist in setting up "conda" environments that will simplify the gathering of Python libraries and version specific to the tutorial you are working on.

### Installing Miniconda

##### Windows
Click [here](http://conda.pydata.org/miniconda.html) to download the proper installer for your Windows platform (64 bits).
We recommend to download the Python 3 version of Miniconda. You can still create Python 2 environments using the Python 3 version of Miniconda.

When installing, you will be asked if you wish to make the Anaconda Python your default Python for Windows.
If you do not have any other installation that is a good option. If you want to keep multiple versions of python on your machine (e.g. ESRI-supplied python, or 64 bit versions of Anaconda), then don't select the option to modify your path or modify your windows registry settings.

##### Linux and OSX
You may follow manual steps from [here](http://conda.pydata.org/miniconda.html) similar to the instructions on Windows (see above). Alternatively, you can execute these commands on a terminal shell (in this case, the bash shell):

```bash
# For MacOSX
url=https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
# For Linux
url=https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
wget $url -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
conda update conda --yes
```

### Installing Anaconda (Optional)

*NOTE: If you don't have time or disk space for the entire distribution do not install Anaconda. Install only [Miniconda](http://conda.pydata.org/miniconda.html), a bootstrap version of Anaconda, which contains only Python, essential packages, and conda. We will provide an environment file to install all the packages necessary for the hackweek.*

[Anaconda](https://www.anaconda.com/distribution/) is a data science platform that comes with a lot of packages. At its core, Anaconda uses the conda package management system.

The list of packages included can be found [*here*](https://docs.anaconda.com/anaconda/packages/pkg-docs)

1. To install Anaconda, please click on the link below for your operating system, and follow the instructions on the [site](https://www.anaconda.com/download/).
2. Once Anaconda installation step is finished run `python` in the command line to test if Anaconda is installed correctly. **Note: For windows, please use the Anaconda prompt as the command line. It should be installed with your installation of Anaconda**
If Anaconda is installed correctly, you should have this prompt, which emphasizes **Anaconda**:

```bash
$ python
Python 3.7.3|Anaconda custom (x86_64)| (default, Mar 27 2019, 22:11:17)
...
```

### Installing Python

We will be using Python 3.6 or 3.7 during the week (either will work). Since Anaconda (on Linux) expects you to work in the "bash" shell, if this is not already your default shell, you need to set it to be so (use the "chsh -s /bin/bash" command to change your default shell to bash) or just run an instance of bash from the command line before issuing "Conda" commands (/bin/bash or where it is located on your system).

If you are already familiar with Python 2.7, you can take a look at the syntax differences [here](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html), but the main point to remember is to put the print statements in parentheses:
```python
print('Hello World!')
```


``` bash
$ conda create -n py37 python=3.7
```

To use Python 3.7: 

``` bash
$ conda activate py37
```

To check if you have the correct version: 

``` bash
$ python --version
```


