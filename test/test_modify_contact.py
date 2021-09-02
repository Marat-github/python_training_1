
from model.contact import Contact


def test_modify_first_contact_fname(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(nick_name="TEST"))
    app.contact.modify_first_contact(Contact(first_name="OLEEEEEEEG"))


def test_modify_first_contact_mname(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(nick_name="TEST"))
    app.contact.modify_first_contact(Contact(middle_name="IVANOV"))


def test_modify_first_contact_lname(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(nick_name="TEST"))
    app.contact.modify_first_contact(Contact(last_name="IVANOV"))


def test_modify_first_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(nick_name="TEST"))
    app.contact.modify_first_contact(Contact(bday="10"))