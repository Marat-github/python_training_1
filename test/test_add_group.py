# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="new_group_1", header="new_group_header_1", footer="new_group_footer_1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
