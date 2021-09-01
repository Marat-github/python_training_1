# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.fill_new_contact(Contact(first_name="1234", middle_name="1243", last_name="234", nick_name="324", title="324234",
                              company="fdge", address="ebebebt", home_phone="4532532", mobile_phone="5435435435",
                              work_phone="234324", fax="12333", email="bteby56@mail.ru", email2="bteby56@mail.ru",
                              email3="bteby56@mail.ru", home_page="bteby56@mail.ru", bday="10", bmonth="November",
                              byear="1999", aday="12", amonth="December", ayear="2018", contacts_group="[none]",
                              address2="greg3g43", phone2="32g4", notes="vbfdbr"))


def test_add_empty_contact(app):
    app.contact.fill_new_contact(Contact(first_name="", middle_name="", last_name="", nick_name="", title="",
                              company="", address="", home_phone="", mobile_phone="",
                              work_phone="", fax="", email="", email2="",
                              email3="", home_page="", bday="-", bmonth="-",
                              byear="", aday="-", amonth="-", ayear="", contacts_group="[none]",
                              address2="", phone2="", notes=""))
