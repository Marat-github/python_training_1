
from model.contact import Contact
from random import randrange


def test_modify_some_contact_fname(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(nick_name="TEST"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="4444")
    contact.id = old_contacts[index].id
    contact.last_name = old_contacts[index].last_name
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
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