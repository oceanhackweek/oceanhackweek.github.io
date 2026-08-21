# Compute FAQ

Quick answers for getting onto the hub at OHW26. For the full walkthrough with screenshots, see the [JupyterHub preparation page](../../resources/prep/jupyterhub.md).

## What are we using for compute?

[CryoCloud](https://book.cryointhecloud.com/) — a community JupyterHub, run on [2i2c](https://2i2c.org) infrastructure, where we can set up pre-configured compute environments for the tutorials. We use it for tutorials and for project work.

The hub is at [https://hub.cryointhecloud.com](https://hub.cryointhecloud.com).

## What do I need to do before I log in?

Two things, both on GitHub:

1. **Accept the invitation** to the [OceanHackWeek GitHub organization](https://github.com/oceanhackweek), so that you show up in [`ohw26-participants`](https://github.com/orgs/oceanhackweek/teams/ohw26-participants).
2. **Make your organization membership public.** Find yourself on the team page above, open your profile within the organization (a URL like `https://github.com/orgs/oceanhackweek/people/YOUR-USERNAME`), and check that **Membership** reads `public` rather than `private`.

CryoCloud works out what you can access from your GitHub team membership, so it can't see you if your membership is private.

## What happens the first time I log in?

GitHub will ask you to **authorize `nasa-cryo-prod`** (the CryoCloud deployment, run by 2i2c) to read your organization and team membership.

```{admonition} Grant access to the oceanhackweek organization
:class: important

On the authorization screen, make sure **`oceanhackweek`** is granted — if it shows an `✕` with a **Grant** button next to it, click **Grant** before you authorize.
```

## Which environment and how much RAM should I pick?

You choose both on the **Server Options** page, every time you start a server:

- **Environment** — the **OceanHackWeek Python Image** for the tutorials and most project work. If you're working in R, pick the **Py-Rocket** R image instead.
- **Resource Allocation** — **8 GB of RAM** should be enough for the tutorials. Pick the smallest allocation that does the job; the compute is shared and donated.

## Why is it taking so long to start?

Starting a new node and pulling our environment can take several minutes, especially when everyone logs in at once at the beginning of a tutorial. Be patient rather than reloading repeatedly.

## How do I get the tutorials?

Use the nbgitpuller link for the profile you're running:

::::{tab-set}

:::{tab-item} Python

[Pull the tutorials into JupyterLab](https://hub.cryointhecloud.com/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Foceanhackweek%2Fohw-tutorials&urlpath=lab%2Ftree%2Fohw-tutorials%2F&branch=OHW26)

:::

:::{tab-item} R

[Pull the tutorials into RStudio](https://hub.cryointhecloud.com/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Foceanhackweek%2Fohw-tutorials&urlpath=rstudio%2F&branch=OHW26)

:::

::::

Clicking the link again later will pull in any updates and merge them with your own changes. See the [extended discussion](../../resources/prep/jupyterhub.md#how-do-i-get-the-tutorial-repository) for the details, and for the `git`-based alternative.

## What should I do when I'm finished for the day?

**Please shut down your server.** Go to `File > Hub Control Panel` (or straight to [https://hub.cryointhecloud.com/hub/home](https://hub.cryointhecloud.com/hub/home) if you've closed the tab), then click **Stop My Server**.

`File > Log Out` does *not* shut the server down.

```{admonition} You will not lose your work
:class: important

Stopping your server does **not** delete any of your files. It just releases the compute, like turning off your desktop at the end of the day.
```

## Can I keep using CryoCloud after OceanHackWeek?

Yes. Go through CryoCloud's own [getting started instructions](https://book.cryointhecloud.com/getting-started/), including the survey. You'll be invited to their Slack channel, which is how the hub admins and users stay in touch.

Two notes on that form:

- **Award number** — if you don't have a grant number, enter `OceanHackWeek`. It doesn't bill any grant; it's used for tracking and for justifying their compute credits.
- **Institution** — the list is a bit US-centric at the moment. If one of the options is a reasonable match but there's a better term for your situation, put that down under *Other*, so the form can be improved.

## Something's broken and this page didn't help

Ask in the `#ohw26_helpdesk` Slack channel and tag `@help-infrastructure`. See the [Getting Help page](getting_help.md) for the other help groups.
