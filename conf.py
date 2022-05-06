# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

# Load local extensions
sys.path.append(os.path.abspath("./_ext"))

# -- Project information -----------------------------------------------------

project = "OceanHackWeek"
author = "OceanHackWeek contributors"
# -- Sphinx config ---------------------------------------------------
extensions = [
    "myst_nb",
    # "myst_parser",
    "ablog",
    "sphinx_design",
    "ohw_team",
]

# sphinx_panels config
panels_add_bootstrap_css = True

templates_path = ["_templates"]
pygments_style = "sphinx"
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "*import_posts*",
    "**/pandoc_ipynb/inputs/*",
    "ipynb_checkpoints/*",
    "posts/**/.ipynb_checkpoints/*",
    ".github/*",
    ".history",
    "github_submodule/*",
    "LICENSE.md",
    "README.md",
    "jupyter_execute/**/*",
    "_InstructionSiteUpdates.md",
]
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# I'm using a custom footer in _templates
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True
copyright = "2022, OceanHackWeek"


# -- HTML Config -------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "search_bar_text": "Search this site...",
    # "google_analytics_id": "",
    "navbar_end": ["search-field.html", "navbar-icon-links"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/oceanhackweek/",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/oceanhackweek",
            "icon": "fab fa-twitter-square",
        },
        {
            "name": "YouTube",
            "url": "https://www.youtube.com/playlist?list=PLA6PlfxWZPLTPQ_OIr3dDPF9FRiHQXoVF",
            "icon": "fab fa-youtube-square",
        },
        {"name": "Email", "url": "mailto:oceanhkw@uw.edu", "icon": "fas fa-envelope"},
    ],
    "use_edit_page_button": True,
}
html_scaled_image_link = False

html_context = {
    "github_user": "oceanhackweek",
    "github_repo": "oceanhackweek.github.io",
    "github_version": "source",
}


# html_favicon = "_static/magnifying.ico"
html_static_path = ["_static"]
html_sidebars = {
    "index": [
        "hello.html",
        # "recentposts.html"
    ],
    "about": ["hello.html"],
    "posts/**": [
        "hello.html",
        "recentposts.html",
        "archives.html",
        # "tags.html"
    ],
    "**": [
        "hello.html",
        # "search-field.html",
        "sidebar-nav-bs.html",
        # "recentposts.html",
        # "archives.html", "tags.html"
    ],
}
blog_baseurl = ""
blog_title = "OceanHackWeek"
blog_path = "posts"
fontawesome_included = True
blog_post_pattern = "posts/**/*"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 1
post_date_format = "%d %B %Y"

# -- Myst config ---------------------------------------------------
myst_admonition_enable = True
myst_deflist_enable = True
myst_update_mathjax = False
myst_enable_extensions = ["substitution", "colon_fence"]

# panels_add_bootstrap_css = False

extensions += ["ablog"]

# Temporarily stored as off until we fix it
jupyter_execute_notebooks = "off"  # TODO test


def setup(app):
    app.add_css_file("custom.css")
