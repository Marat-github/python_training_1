

def test_email_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[1]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
