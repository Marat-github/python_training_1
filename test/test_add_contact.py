# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return  prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    number = string.digits
    return "".join([random.choice(number) for i in range(random.randrange(maxlen))])


def random_month():
    month = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
    return "".join(month[random.randint(0, 11)])


testData = [Contact(first_name="", middle_name="", last_name="", nick_name="", title="", company="", address="",
                    home_phone="", mobile_phone="",work_phone="", fax="", email="", email2="", email3="",
                    home_page="", bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="", address2="",
                    phone2="", notes="")] + [
    Contact(first_name=random_string("name", 10), middle_name=random_string("middle", 10), last_name=random_string("last", 10),
            nick_name=random_string("nick", 10), title=random_string("", 20), company=random_string("", 10), address=random_string("", 20),
            home_phone=random_number(9), mobile_phone=random_number(9), work_phone=random_number(9), fax=random_number(6),
            email=random_string("", 10), email2=random_string("", 10), email3=random_string("", 10), home_page=random_string("", 10),
            bday=random.randint(1,31), bmonth=random_month(), byear=random_number(4), aday=random.randint(1,31), amonth=random_month(),
            ayear=random_number(4), address2=random_string("middle", 10), phone2=random_number(9), notes=random_string("", 30))
    for i in range(5)
]

'''
testData = [
    Contact(first_name=fname, middle_name=mname, last_name=lname, nick_name=nick, title=title, company=comp,
            address=addr, home_phone=hphone, mobile_phone=mphone, work_phone=wphone, fax=fax, email=email,
            email2=email2, email3=email3, home_page=hpage, bday=bday, bmonth=bmonth, byear=byear, aday=aday,
            amonth=amonth, ayear=ayear, address2=addr2, phone2=phone2, notes=notes)
    for fname in ["", random_string("FName", 10)]
    for mname in ["", random_string("MName", 10)]
    for lname in ["", random_string("LName", 10)]
    for lname in ["", random_string("LName", 10)]
    for nick in ["", random_string("LName", 10)]
    for title in ["", random_string("title", 10)]
    for comp in ["", random_string("company", 10)]
    for addr in ["", random_string("adress", 30)]
    for hphone in ["", random_number(10)]
    for mphone in ["", random_number(10)]
    for wphone in ["", random_number(10)]
    for fax in ["", random_number(6)]
    for email in ["", random_string("email@", 20)]
    for email2 in ["", random_string("email2@", 20)]
    for email3 in ["", random_string("email3@", 20)]
    for hpage in ["", random_string("homapage", 15)]
    for bday in ["", str(random.randint(1, 31))]
    for bmonth in ["", random_month()]
    for byear in ["", random_number(4)]
    for aday in ["", str(random.randint(1, 31))]
    for amonth in ["", random_month()]
    for ayear in ["", random_number(4)]
    for addr2 in ["", random_string("name", 30)]
    for phone2 in ["", random_number(10)]
    for notes in ["", random_string("notes:", 30)]
]
'''


@pytest.mark.parametrize("contact", testData, ids=[repr(x) for x in testData])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
