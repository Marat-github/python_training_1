from sys import maxsize


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nick_name=None, title=None, company=None, address=None, home_phone=None,
                 mobile_phone=None, work_phone=None, fax=None, email=None, email2=None, email3=None, home_page=None, bday=None, bmonth=None, byear=None,
                 aday=None, amonth=None, ayear=None, address2=None, phone2=None, notes=None, id=None, all_phones_from_home_page=None, all_email_from_home_page=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.home_page = home_page
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s---%s---%s---%s---%s---%s" % (self.id, self.last_name, self.first_name, self.mobile_phone, self.bday, self.bmonth)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and\
               self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize