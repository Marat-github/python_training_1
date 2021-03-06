from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create_new_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_home_page()
        self.contact_cache = None

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def type_date(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.first_name)
        self.type("middlename", contact.middle_name)
        self.type("lastname", contact.last_name)
        self.type("nickname", contact.nick_name)
        self.type("title", contact.title)
        self.type("company", contact.company)
        self.type("address", contact.address)
        self.type("home", contact.home_phone)
        self.type("mobile", contact.mobile_phone)
        self.type("address", contact.address)
        self.type("work", contact.work_phone)
        self.type("fax", contact.fax)
        self.type("email", contact.email)
        self.type("email2", contact.email2)
        self.type("email3", contact.email3)
        self.type("homepage", contact.home_page)
        self.type_date("bday", contact.bday)
        self.type_date("bmonth", contact.bmonth)
        self.type("byear", contact.byear)
        self.type_date("aday", contact.aday)
        self.type_date("amonth", contact.amonth)
        self.type("ayear", contact.ayear)
        self.type("address2", contact.address2)
        self.type("phone2", contact.phone2)
        self.type("notes", contact.notes)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_elements_by_css_selector('[href^="edit.php?id="]')[index].click()
        # wd.find_elements_by_css_selector('#maintable > tbody:nth-child(1) > tr > td:nth-child(8) > a:nth-child(1)')\
        # [index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None

    def return_home_page(self):
        wd = self.app.wd
        # return to main page
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            wd.find_element_by_link_text("home").click()
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                # id
                contact_id = element.find_element_by_name('selected[]').get_attribute("value")
                # last name
                l_name = element.find_element_by_css_selector('tbody > tr > td:nth-child(2)').text
                # first name
                f_name = element.find_element_by_css_selector('tbody > tr > td:nth-child(3)').text
                # address
                addr = element.find_element_by_css_selector('tbody > tr > td:nth-child(4)').text
                # all phones
                all_phones = element.find_elements_by_tag_name("td")[5].text
                # all email
                all_email = element.find_elements_by_tag_name("td")[4].text
                self.contact_cache.append(Contact(first_name=f_name, last_name=l_name, id=contact_id,
                                                  all_phones_from_home_page=all_phones, address=addr,
                                                  all_email_from_home_page=all_email))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_elements_by_css_selector('[href^="edit.php?id="]')[index].click()
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        addr = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id=id, home_phone=homephone, work_phone=workphone,
                       mobile_phone=mobilephone, phone2=secondphone, address=addr, email=email, email2=email2,
                       email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_elements_by_css_selector('[href^="view.php?id="]')[index].click()
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=homephone, work_phone=workphone, mobile_phone=mobilephone, phone2=secondaryphone)
