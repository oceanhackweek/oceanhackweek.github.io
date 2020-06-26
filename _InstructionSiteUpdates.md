# Editing OHW web site content and layout

The OceanHackweek web site is a Jekyll site that uses the [Jekyll Spectral theme.](http://jekyllthemes.org/themes/spectral/)

## Location of main content documents

Relevant, editable content is organized in the following directories and files:

- [_config.yml](https://github.com/oceanhackweek/oceanhackweek.github.io/blob/source/_config.yml): core Jekyll site configuration, including some banner/header/footer text and urls
- [jekyll-spectral-theme/_includes](https://github.com/oceanhackweek/oceanhackweek.github.io/tree/source/jekyll-spectral-theme/_includes) directory: front page content, broken up into sections, one markdown file per section.
  - The layout templates for sections and section order are controlled by [jekyll-spectral-theme/_layouts/default.html](https://github.com/oceanhackweek/oceanhackweek.github.io/blob/source/jekyll-spectral-theme/_layouts/default.html)
  - Each section specifies a template for its layout, where the templates available are found in [jekyll-spectral-theme/_layouts](https://github.com/oceanhackweek/oceanhackweek.github.io/tree/source/jekyll-spectral-theme/_layouts)
  - Section two ("Information for Applicants") is a special beast. While [jekyll-spectral-theme/_includes/section-02.html](https://github.com/oceanhackweek/oceanhackweek.github.io/blob/source/jekyll-spectral-theme/_includes/section-two.html) orchestrates it, the directives there point to content to be grabbed from tags `title` and `description` in [_pages/01-applicants.md](https://github.com/oceanhackweek/oceanhackweek.github.io/blob/source/_pages/01-applicants.md)
- [_pages](https://github.com/oceanhackweek/oceanhackweek.github.io/tree/source/_pages): content for extra pages, including all the pages accessible via the drop-down menu on the upper right of the page.
  - The destination page file name (what a user sees) is *not* the source markdown file name on the repository; instead, the destination file name is found in the `permalink` tag within the markdown file. For example, for [_pages/01-applicants.md](https://github.com/oceanhackweek/oceanhackweek.github.io/blob/source/_pages/01-applicants.md), the destination file name is [applicant-info.html](https://oceanhackweek.github.io/applicant-info.html)

Note that apparently any Markdown file dropped at the root level of the repository, or in the `_pages` directory (or possibly anywhere else?), will be automatically added to the Menu drop down; except ones with names starting with the `_` character.

## Editing and testing locally (in your computer) with Jekyll

Clone the GitHub repo locally, then edit the content of files following the documentation in the previous section. To view your changes, rebuild the site using Jekyll.

Install Jekyll locally through conda with:

```shell
conda create --name JEKYLL -c conda-forge rb-bundler compilers
conda activate JEKYLL
bundle install
```

To build and serve the site, run this statement:

```shell
bundle exec jekyll serve
```

The site will be available at `http://127.0.0.1:4000/`.

Note that the main branch is actually called `source`, not `master`! Ignore the `master` branch (we may delete it later).
