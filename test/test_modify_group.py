
from model.group import Group


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="NAME_after_modify"))


def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="HEADER_after_modify"))
