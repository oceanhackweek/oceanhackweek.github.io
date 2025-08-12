# Editing OHW web site content and layout

The OceanHackweek web site uses [Sphinx](https://www.sphinx-doc.org/en/master/) with the [PyData theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/index.html) and [Ablog](https://ablog.readthedocs.io/en/latest/) for adding posts.

For quick changes to single pages, you can make edits directly via Github, or to make deeper changes you can work locally.

## Via Github

Github is great for making small changes such as helping to clean up spelling mistakes.

### Edit this page

On most pages of the site there is a right hand sidebar (you may need to expand your screen or decrease your font size to see it).
At the bottom of the sidebar, there is a link to __Edit this page__.

If you click the __Edit this page__, you'll be taken to the source of the page on Github.

### Navigating Github

The code for the website is stored in the [`oceanhackweek/oceanhackweek.github.io](https://github.com/oceanhackweek/oceanhackweek.github.io) repo. The folder structure largely mimics the path structure on the website, but see _Location of main content documents_ below for specifics.

Once you've found the page, there is a pencil icon in the top right to move into editing mode.

### Making edits

Most of the pages in the site are Markdown documents with some MyST formatting (see below). While Github can preview the changes to the Markdown, but it cannot parse the MyST, so it is likely to display some funky code blocks in their place. Once you create a PR, you'll get an accurate preview of changes.

### Creating a Pull Request

Once you think you are happy with your edits, give the changes a name, and optionally a description (for example referencing an issue number that the change takes care of).

Then select __Create a new branch for this commit and start a pull request__ to create a PR.

Github will take the title and description from the commit to start your PR, but it's also a good place to discuss the changes further. 

Please include `@oceanhackweek/website` in the PR description so the website team gets a notification about the PR.

Once you create a PR Netlify will generate a preview site using much of the same build commands as the public website. This will allow you (and us) to see the exact effects of your changes.

## Locally

For larger changes, or working with MyST, rST, or Jupyter Notebooks, it's easier to work on the website locally.

### Setup for local development

There are a few steps to get started with local development.

#### Forking the repo

The first step to work on the repo is to create your own fork.
On [`oceanhackweek/oceanhackweek.github.io](https://github.com/oceanhackweek/oceanhackweek.github.io) click __Fork__ in the upper right corner and create the fork in your personal github account.

Then click __Code__ and clone the repo to your machine. (The Github CLI is nice for working with forks).

It is worth noting that we are using the `source` branch as the base for this repo, but it is best to create a new branch to work off of for each set of changes and propose them in a Pull Request.

#### Environment

There is a pre-configured conda environment in `pixi.toml`.
To use it, prefix commands with `pixi run` to make sure the environment is up to date.

#### Commands

- `pixi run live` - The environment is setup with [sphinx-autobuild](https://pypi.org/project/sphinx-autobuild/) which will update open browsers when files are saved. The site will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
- `pixi run html` - Launch a one off build of HTML output.
- `pixi run clean` - Clean all the build directories. This can be useful as Sphinx tries to do incremental builds, and sometimes it will end up out of sync.
- `git pull upstream source` to bring in any changes from the main repo.

### Writing and Linking Pages

Pages can be written as ReStructured Text, Markdown, or Jupyter Notebooks thanks to [MyST-NB](https://myst-nb.readthedocs.io/en/latest/).

To include a page into the site navigation, it needs to be included in a `toctree`.
In most cases the `toctree`s will be found in one of the `index.md` pages.
The `toctree` on the top level `index.md` controls the horizontal navigation at the top of the site, all other `toctree`s create the left sidebar navigation (the right sidebar navigation is created from headers within a page).

From `./index.md`:
````md
```{toctree}
:maxdepth: 2
:hidden:
about/index.md
2022/index.md
resources/index.md
posts
```
````

### Writing Posts

Like pages, posts can be written as ReStructured Text, Markdown, or Jupyter notebooks. To be treated as a post, they need to be within the `posts/` directory, and have a selection of metadata.

The location and structure of the metadata varies depending on filetype. For a full list of the options, see the [ABlog](https://ablog.readthedocs.io/en/latest/manual/posting-and-listing/) documentation.

#### Markdown

In Markdown, the metadata to create a post can be added as YAML frontmatter.

For example:

```md
---
date: 2021-08-07
title: OceanHackWeek 2021 @ Bigelow Labs Recap
tags: event, recap, OHW21
category: Event
author: Alex Kerney
---
# OceanHackWeek 2021 @ Bigelow Labs

_the rest of the post below_
```

The only required metadata tag to make a post is `date`. The rest will either be extracted from the post (the title), derived from `conf.py` (authors), or treated as null (tags and comments).

##### Directives

MyST-NB/MyST-Parser brings ReStructured Text style directive support to Markdown.
The `toctree` above is one example, but rather than listing all possibilities, here are some resources:
- [Jupyterbook - MyST Markdown Overview](https://jupyterbook.org/en/stable/content/myst.html)
- [MyST syntax guide](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html)
- [Sphinx - Directives](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html)
- [ReStructued Text - Directives](https://docutils.sourceforge.io/docs/ref/rst/directives.html)

#### ReStructured Text

ReStructured Text can be written as usual for Sphinx documentation.

#### Jupyter Notebooks

It's a little sneaky to make a Jupyter notebook into a post. The metadata needs to be added to the notebook metadata. 

In JupyterLab, you can do this by clicking the gear at the top of the right sidebar, then expand the _Advanced Tools_ section.

Then you will see a JSON object with lots distracting Jupyter metadata.

```json
{
    "kernelspec": {
        "display_name": "Python 3 (ipykernel)",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "codemirror_mode": {
            "name": "ipython",
            "version": 3
        },
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.7.3"
    },
}
```

To turn it into a post, `date` and `title` keys needs to be added in addition to having the notebook within the `posts/` directory. I'd suggest `author`, `category`, and `tags` as well.

```diff
{
    "kernelspec": {
        "display_name": "Python 3 (ipykernel)",
        "language": "python",
        "name": "python3"
    },
    "language_info": {
        "codemirror_mode": {
            "name": "ipython",
            "version": 3
        },
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.7.3"
    },
+    "author": "Alex Kerney",
+    "date": "2021-11-02",
+    "title": "A notebook post",
+    "tags": [
+      "notebook",
+      "demo"
+    ],
+    "category": "Projects"
}
```

It's worth noting that Jupyter is strict about JSON formatting, and it will not
save the changes unless the formatting is correct.
Namely that means not having trailing `,`s in objects or arrays.
Once you start editing, you will see a revert or undo symbol show up at the top of the metadata box.
When the JSON is valid, there will also be a checkmark.
Click the check, then save the notebook for Sphinx/ABlog to find it.

### Pull Requests

Once you've made your changes, create a Pull Request to suggest that we include them in the website.

Include a description of what the changes are, and maybe a screenshot to help describe them.

Please tag `@oceanhackweek/website` to notify the website maintainers that you've made a PR. If you make a draft PR, you can wait until you are ready, then tag the website maintainers.

After you create a PR, Netlify will build the site and make a comment with a link to preview your changes. This also makes it easier for us to review the changes, and for you to share them with others.

## Location of main content documents

While most pages follow the same structure in the repo, as they do on the website, there are a few additional files to be aware of:

- `conf.pd` - This is the Sphinx configuration file.
- `pixi.toml` - The conda environment needed to build the website.
- `requirements.txt` - A pip installable environment to build the website. This is mainly used by Netlify to create previews of Pull Requests. It is generated with `pip list --format=freeze > requirements.txt`
- `posts.md` - A stub page that is replaced when blog posts are generated.
- `_build/` - Automatically generated output from Sphinx.
  - `html/` - The HTML generated by Sphinx for the website.
- `_static/` - Various files that need to be included into the website.
- `_templates/` - A collection of Jinja2 templates to control page styling.
- `_ext/` - Custom Sphinx extensions.
  - `ohw_team.py` - Sphinx extension to allow quick embedding of team member info.
  - `team.yaml` - Team member information.
