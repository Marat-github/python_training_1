from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    number = string.digits
    return "".join([random.choice(number) for i in range(random.randrange(maxlen))])


def random_month():
    month = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
    return "".join(month[random.randint(0, 11)])


def random_day(month):
    if month == "December" or month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October":
        return random.randint(1,31)
    elif month == "February":
        return random.randint(1, 29)
    else:
        return random.randint(1, 30)


testData = [Contact(first_name="", middle_name="", last_name="", nick_name="", title="", company="", address="",
                    home_phone="", mobile_phone="",work_phone="", fax="", email="", email2="", email3="",
                    home_page="", bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="", address2="",
                    phone2="", notes="")] + [
    Contact(first_name=random_string("name", 10), middle_name=random_string("middle", 10), last_name=random_string("last", 10),
            nick_name=random_string("nick", 10), title=random_string("", 20), company=random_string("", 10), address=random_string("", 20),
            home_phone=random_number(9), mobile_phone=random_number(9), work_phone=random_number(9), fax=random_number(6),
            email=random_string("", 10), email2=random_string("", 10), email3=random_string("", 10), home_page=random_string("", 10),
            bmonth=random_month(), bday=str(random.randint(1,31)), byear=random_number(4), aday=str(random.randint(1,31)), amonth=random_month(),
            ayear=random_number(4), address2=random_string("middle", 10), phone2=random_number(9), notes=random_string("", 30))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    out.write(json.dumps(testData, default=lambda x: x.__dict__, indent=2))