from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from sphinx_design.badges_buttons import create_bdg_classes
import yaml


def load_team_info():
    with open("./_ext/team.yaml") as f:
        return yaml.safe_load(f.read())["team"]


class OHWTeam(SphinxDirective):
    """
    Adds a directive that allows the display of team members,
    and allows the filtering by what roles they are involved in,
    and can optionally show badges for those roles.

    ```{ohw-team}
    :roles: Steering Committee,Infrastructure
    :badges:
    ```

    If `:roles: all` then everyone will be displayed.
    """

    has_content = True
    option_spec = {"roles": directives.unchanged_required, "badges": directives.flag}

    def run(self):
        team = load_team_info()

        if self.options["roles"] == "all":
            members_in_roles = team
        else:
            roles = set(self.options["roles"].split(","))

            members_in_roles = []
            for member in team:
                try:
                    member_roles = set(member["roles"])

                    if member_roles.intersection(roles):
                        members_in_roles.append(member)
                except KeyError:
                    pass

        row = nodes.container(is_div=True, classes=["row"])

        for member in members_in_roles:
            col = nodes.container(is_div=True, classes=["col-4", "mb-1"])
            card = nodes.container(is_div=True, classes=["card"])
            card.append(
                nodes.image(
                    uri=member["image_url"],
                    alt=member["name"],
                    classes=["card-image-top"],
                )
            )
            body = nodes.container(is_div=True, classes=["card-body"])
            name = nodes.paragraph(text=member["name"], classes=["h5"])

            if "github_user" in member and member["github_user"] is not None:
                target = directives.uri("https://github.com/" + member["github_user"])
                link = nodes.reference(
                    "", refuri=target, text="", classes=["fab", "fa-github", "ml-1"]
                )
                link.append(nodes.inline(text=""))
                name.append(link)

            body.extend(
                [
                    name,
                    nodes.inline(text=f'{member["title"]} - '),
                    nodes.emphasis(text=member["affiliate"]),
                ]
            )

            if "badges" in self.options:
                badges = nodes.container(is_div=True)
                body.append(badges)
                try:
                    for role in member["roles"]:
                        badges.append(
                            nodes.inline(
                                text=role, classes=create_bdg_classes("primary", False)
                            )
                        )
                except KeyError:
                    pass

            card.append(body)
            col.append(card)
            row.append(col)

        return [row]


def setup(app: Sphinx):
    app.add_directive("ohw-team", OHWTeam)

    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
