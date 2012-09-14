#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from base import Base

def create_eyedee_user_by_api(username, password):
    import requests
    import json
    headers = {'content-type': 'application/json'}
    params = {
        'user': username,
        'pass': password
    }
    result = requests.post(
        'http://eyedee.me/api/signin', 
        data=json.dumps(params),
        headers=headers)

    assert result.status_code == requests.codes.ok
    print result.text

class eyedee(Base):

    _page_url = 'http://eyedee.me'
    _username_locator = (By.ID, 'username')
    _create_password_locator = (By.CSS_SELECTOR, 'div#signup #password')
    _new_password_locator = (By.ID, 'new_password')
    _main_password_locator = (By.CSS_SELECTOR, 'div#main #password')
    _sign_up_link_locator = (By.CSS_SELECTOR, 'a.signin')
    _sign_up_button_locator = (By.CSS_SELECTOR, 'div#signup form > button') # change to #sign_in
    _sign_in_button_locator = (By.ID, 'sign_in')
    _create_account_locator = (By.ID, 'create_account')

    def __init__(self, selenium, timeout=60, handle=None):
        Base.__init__(self, selenium=selenium, timeout=timeout, handle=handle)
        # if this is created by the SignIn popup, handle will be passed in
        # and this class will use the existing popup.
        # if this is created by the ServerSignIn, handle will not be passed
        # and the popup will be searched for.
        if not handle:
            time.sleep(15)
            for handle in selenium.window_handles:
                selenium.switch_to_window(handle)
                if 'EyeDee.Me' in selenium.title:
                    break
        # selenium.switch_to_window('__persona_dialog')  ## need window name here

    def open_page(self):
        self.selenium.get(self._page_url)
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._sign_up_link_locator).is_displayed())
        self.selenium.find_element(*self._sign_up_link_locator).click()

    @property
    def username(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._username_locator).is_displayed())
        return self.selenium.find_element(*self._username_locator).get_attribute('value')

    @username.setter
    def username(self, value):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._username_locator).is_displayed())
        field = self.selenium.find_element(*self._username_locator)
        field.clear()
        field.send_keys(value)

    # eyedee.me has 3 different password fields with the same id
    # - sign up
    # - sign in
    # - create user

    @property
    def password(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._main_password_locator).is_displayed())
        return self.selenium.find_element(*self._main_password_locator).get_attribute('value')

    @password.setter
    def password(self, value):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._main_password_locator).is_displayed())
        # really really sure...
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._main_password_locator).is_displayed())
        field = self.selenium.find_element(*self._main_password_locator)
        field.clear()
        field.send_keys(value)

    @property
    def create_password(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._create_password_locator).is_displayed())
        return self.selenium.find_element(*self._create_password_locator).get_attribute('value')

    @create_password.setter
    def create_password(self, value):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._create_password_locator).is_displayed())
        field = self.selenium.find_element(*self._create_password_locator)
        field.clear()
        field.send_keys(value)

    @property
    def new_password(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._new_password_locator).is_displayed())
        return self.selenium.find_element(*self._new_password_locator).get_attribute('value')

    @new_password.setter
    def new_password(self, value):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._new_password_locator).is_displayed())
        field = self.selenium.find_element(*self._new_password_locator)
        field.clear()
        field.send_keys(value)

    def click_create_account(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._create_account_locator).is_displayed())
        self.selenium.find_element(*self._create_account_locator).click()
        # XXX it would be nice to wait for something here
        # but i can't get the popup to hold still long enough
        # to figure out what
        time.sleep(10)
        self.switch_to_main_window()

    def click_sign_up(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._sign_up_button_locator).is_displayed())
        self.selenium.find_element(*self._sign_up_button_locator).click()
        time.sleep(10)
        self.switch_to_main_window()

    def click_sign_in(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._sign_in_button_locator).is_displayed())
        self.selenium.find_element(*self._sign_in_button_locator).click()
        time.sleep(10)
        self.switch_to_main_window()

    def create_user(self, username, password):
        self.open_page()
        self.username = username
        self.create_password = password
        self.click_sign_up()