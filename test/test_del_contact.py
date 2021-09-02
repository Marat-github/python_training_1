
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(nick_name="TEST"))
    app.contact.test_delete_first_contact()
