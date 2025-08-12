import fnmatch

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

    Role filtering also supports glob style matching, so `OHW22 Organizer*`
    should match anyone involved with OHW22 even if the role name is longer.

    Github icons will be shown if `github_user` is provided in the team.yaml

    Emails can be shown as links or icons with `email_link` or `email_icon`
    if `email` is set in team.yaml.

    ```{ohw-team}
    :roles: Steering Committee,Infrastructure
    :badges:
    ```

    If `:roles: all` then everyone will be displayed.
    """

    has_content = True
    option_spec = {
        "roles": directives.unchanged_required,
        "hide_role_badges": directives.unchanged,
        "badges": directives.flag,
        "email_icon": directives.flag,
        "email_link": directives.flag,
    }

    def run(self):
        team = load_team_info()
        try:
            hide_role_badges = self.options["hide_role_badges"].split(",")
        except KeyError:
            hide_role_badges = []

        if self.options["roles"] == "all":
            members_in_roles = team
        else:
            roles = self.options["roles"].split(",")

            members_in_roles = []
            for member in team:
                try:
                    member_roles = member["roles"]

                    for role in roles:
                        if any(
                            (
                                fnmatch.fnmatch(member_role, role)
                                for member_role in member_roles
                            )
                        ):
                            members_in_roles.append(member)
                            continue
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
            name = nodes.paragraph(text=member["name"] + " ", classes=["h5"])

            # Add Github icon if github user account is provided
            if "github_user" in member and member["github_user"] is not None:
                target = "https://github.com/" + member["github_user"]
                icon = nodes.inline(text="", classes=["fab", "fa-github", "ml-1"])
                link = nodes.reference("", refuri=target)
                link.append(icon)
                name.append(link)

            # If emails are avaliable and email_icon is enabled, then add a email icon
            if (
                "email_icon" in self.options
                and "email" in member
                and member["email"] is not None
            ):
                target = "mailto:" + member["email"]
                icon = nodes.inline(text="", classes=["fas", "fa-envelope", "ml-1"])
                link = nodes.reference("", refuri=target)
                link.append(icon)
                name.append(link)

            body.extend(
                [
                    name,
                    nodes.inline(text=f'{member["title"]} - '),
                    nodes.emphasis(text=member["affiliate"]),
                ]
            )

            # If emails are avaliable and email_link is enabled, then add a email link
            if (
                "email_link" in self.options
                and "email" in member
                and member["email"] is not None
            ):
                target = directives.uri("mailto://" + member["email"])
                link = nodes.reference("", refuri=target, text=member["email"])
                link.append(nodes.inline(text=member["email"]))
                link_wrapper = nodes.paragraph(text="")
                link_wrapper.append(link)
                body.append(link_wrapper)

            # If badges should be shown, add and style them
            if "badges" in self.options:
                badges = nodes.container(is_div=True)
                body.append(badges)
                try:
                    for role in member["roles"]:
                        if not any(
                            (
                                fnmatch.fnmatch(role, hide_role)
                                for hide_role in hide_role_badges
                            )
                        ):
                            if role == "Steering Committee":
                                color = "primary"
                                outline = False
                            elif (
                                "Organizer" in role
                                or "Instructor" in role
                                or "Leader" in role
                            ):
                                color = "primary"
                                outline = True
                            elif "Participant" in role:
                                color = "secondary"
                                outline = True
                            else:
                                color = "secondary"
                                outline = False

                            badges.append(
                                nodes.inline(
                                    text=role,
                                    classes=[
                                        *create_bdg_classes(color, outline),
                                        "mr-1",
                                    ],
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
