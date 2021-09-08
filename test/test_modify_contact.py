
from model.contact import Contact


def test_modify_first_contact_fname(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(nick_name="TEST"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="OLEEEEEEEG")
    contact.id = old_contacts[0].id
    contact.last_name = old_contacts[0].last_name
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_mname(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(nick_name="TEST"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middle_name="IVANOV"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_first_contact_lname(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(nick_name="TEST"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(last_name="IVANOV"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_first_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(nick_name="TEST"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(bday="10"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)