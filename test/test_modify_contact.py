
from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(first_name="OLEEEEEEEG", middle_name="IGOR", last_name="KOLYA", nick_name="poison",
                                             title="", company="", address="", home_phone="", mobile_phone="",
                                             work_phone="", fax="", email="", email2="", email3="", home_page="",
                                             bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="",
                                             contacts_group="[none]", address2="", phone2="", notes=""))
