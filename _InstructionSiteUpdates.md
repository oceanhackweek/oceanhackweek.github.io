# Editing OHW web site content and layout

The OceanHackweek web site uses [Sphinx](https://www.sphinx-doc.org/en/master/) with the [PyData theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/index.html) and [Ablog](https://ablog.readthedocs.io/en/latest/) for adding posts.

## Getting started

### Environment

There is a pre-configured conda environment in `environment.yml`.
To use it, `conda create env -f=./environment.yml`, then activate with `conda activate ohw-site`.

### Commands

- `make live` - The environment is setup with [sphinx-autobuild](https://pypi.org/project/sphinx-autobuild/) which will update open browsers when files are saved. The site will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
- `make html` - Launch a one off build of HTML output.
- `make clean` - Clean all the build directories. This can be useful as Sphinx tries to do incremental builds, and sometimes it will end up out of sync.

## Writing and Linking Pages

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

## Writing Posts

Like pages, posts can be written as ReStructured Text, Markdown, or Jupyter notebooks. To be treated as a post, they need to be within the `posts/` directory, and have a selection of metadata.

The location and structure of the metadata varies depending on filetype. For a full list of the options, see the [ABlog](https://ablog.readthedocs.io/en/latest/manual/posting-and-listing/) documentation.

### Markdown

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

### ReStructured Text

### Jupyter Notebooks

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

To turn it into a post, `date` and `title` keys needs to be added at a minimum. I'd suggest `author`, `category`, and `tags` as well.

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


## Location of main content documents

Relevant, editable content is organized in the following directories and files:
