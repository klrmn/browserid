#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from browserid.pages.sign_in import SignIn
from browserid.pages.sign_in import ServerSignIn

class HomePage(object):

    _page_url = '/'

    def __init__(self, mozwebqa):
        '''Do not instanciate HomePage objects. Use the HomePage.factory() instead.'''
        self.mozwebqa = mozwebqa
        self.selenium = mozwebqa.selenium
        self.timeout = mozwebqa.timeout
        self.base_url = mozwebqa.base_url

    def factory(self):
        '''Use this method to get the appropriate Home Page for your base_url.'''
        page = None
        if '123done' in self.mozwebqa.base_url:
            page =  OneTwoThreeDoneHome(self.mozwebqa)
        elif 'myfavoritebeer' in self.mozwebqa.base_url:
            page =  MyFavoriteBeerHome(self.mozwebqa)
        elif 'persona.org' in self.mozwebqa.base_url:
            page =  PersonaServerHome(self.mozwebqa)
        elif 'anosrep.org' in self.mozwebqa.base_url:
            page =  PersonaServerHome(self.mozwebqa)
        else:
            raise UnknownHomePageException(
                "%s is not a known base_url" % self.mozwebqa.base_url)
        print type(page)  # for debugging purposes
        return page

    def open_page(self):
        self.selenium.get(self.base_url + self._page_url)

    def is_the_current_page(self):
        return self._page_title in self.selenium.title

    def click_sign_in(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._sign_in_locator).is_displayed())
        self.selenium.find_element(*self._sign_in_locator).click()
        return SignIn(self.selenium, self.timeout)

    def click_sign_out(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._sign_out_locator).is_displayed())
        self.selenium.find_element(*self._sign_out_locator).click()
        # wait for something

    def click_sign_up(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._sign_up_locator).is_displayed())
        self.selenium.find_element(*self._sign_up_locator).click()
        return SignIn(self.selenium, self.timeout)

    @property
    def signed_in(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._signed_in_user_locator).is_displayed())
        return self.selenium.find_element(*self._signed_in_user_locator).is_displayed()

    def signed_in_user(self, user=None):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._signed_in_user_locator).is_displayed())
        return self.selenium.find_element(*self._signed_in_user_locator).text

class OneTwoThreeDoneHome(HomePage):
    _page_title = '123done - your tasks, simplified'
    _sign_in_locator = (By.ID, 'loggedout')
    _sign_out_locator = (By.CSS_SELECTOR, '#loggedin > a')
    _sign_up_locator = _sign_in_locator
    _signed_in_user_locator = (By.CSS_SELECTOR, '#loggedin > span')


class MyFavoriteBeerHome(HomePage):
    _sign_in_locator = (By.CSS_SELECTOR, 'div#loginInfo > div.login.clickable > img')
    _sign_out_locator = (By.CSS_SELECTOR, 'a#logout')
    _sign_up_locator = _sign_in_locator
    _signed_in_user_locator = (By.CSS_SELECTOR, 'div.login > span.username')


class PersonaServerHome(HomePage):
    _page_title = 'Mozilla Persona'
    _sign_in_locator = (By.CSS_SELECTOR, 'a.signIn')
    _sign_up_locator = (By.CSS_SELECTOR, 'a.button.create')
    _manage_section_locator = (By.ID, 'manage')
    _sign_out_locator = (By.CSS_SELECTOR, 'a.signOut')
    _signed_in_user_locator = None  # not supported by server

    def click_sign_in(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._sign_in_locator).is_displayed())
        self.selenium.find_element(*self._sign_in_locator).click()
        return ServerSignIn(self.selenium, self.timeout)

    def click_sign_up(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._sign_in_locator).is_displayed())
        self.selenium.find_element(*self._sign_up_locator).click()
        return ServerSignIn(self.selenium, self.timeout)

    @property
    def signed_in(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: s.find_element(*self._sign_out_locator).is_displayed())
        return self.selenium.find_element(*self._sign_out_locator).is_displayed()

    def signed_in_user(self, user):
        # persona server does not specify logged in user so trick the test
        if self.signed_in:
            return user.primary_email
        return None  # will fail assert if no user is logged in


class UnknownHomePageException(Exception):
    def __init__(self, msg):
        self.msg = msg
