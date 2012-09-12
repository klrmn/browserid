#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from base import Base


class eyedee(Base):

    _page_url = 'http://eyedee.me/#'
    _email_locator = (By.ID, 'email')
    _password_locator = (By.ID, 'password')
    _create_account_locator = (By.CSS_SELECTOR, 'form > div > button.nth-of-type(1)')

    def open_page():
        self.selenium.get(self._page_url)

    @property
    def email(self):
        return self.selenium.find_element(*self._email_locator).get_attribute('value')

    @email.setter
    def email(self, value):
        field = self.selenium.find_element(*self._email_locator)
        field.clear()
        field.send_keys(value)

    @property
    def password(self):
        return self.selenium.find_element(*self._password_locator).get_attribute('value')

    @password.setter
    def password(self, value):
        field = self.selenium.find_element(*self._password_locator)
        field.clear()
        field.send_keys(value)

    def click_create_account(self):
        self.selenium.find_element(*self._create_account_locator).click()

    def create_user(self, username, password):
        self.open_page()
        self.email = username
        self.password = password
        self.click_create_account()