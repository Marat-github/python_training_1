# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="1234", middle_name="1243", last_name="234", nick_name="324", title="324234",
                                           company="fdge", address="ebebebt", home_phone="4532532", mobile_phone="5435435435",
                                           work_phone="234324", fax="12333", email="bteby56@mail.ru", email2="bteby56@mail.ru",
                                           email3="bteby56@mail.ru", home_page="bteby56@mail.ru", bday="10", bmonth="November",
                                           byear="1999", aday="12", amonth="December", ayear="2018", address2="greg3g43",
                                           phone2="32g4", notes="vbfdbr")
    app.contact.create_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="", middle_name="", last_name="", nick_name="", title="",
                                           company="", address="", home_phone="", mobile_phone="",
                                           work_phone="", fax="", email="", email2="",
                                           email3="", home_page="", bday="-", bmonth="-",
                                           byear="", aday="-", amonth="-", ayear="", address2="", phone2="", notes="")
    app.contact.create_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)