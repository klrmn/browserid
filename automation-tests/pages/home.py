#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from browserid.pages.sign_in import SignIn
from browserid.pages.sign_in import ServerSignIn

class HomePage(object):

    def __init__(self, mozwebqa):
        '''Do not instanciate HomePage objects. Use the HomePage.factory() instead.'''
        self.mozwebqa = mozwebqa
        self.selenium = mozwebqa.selenium
        self.timeout = mozwebqa.timeout
        self.base_url = mozwebqa.base_url

    def factory(mozwebqa):
        '''Use this method to get the appropriate Home Page for your base_url.'''
        if '123done' in mozwebqa.base_url:
            return OneTwoThreeDoneHome(mozwebqa)
        elif 'myfavoritebeer' in mozwebqa.base_url:
            return MyFavoriteBeerHome(mozwebqa)
        elif 'persona.org' in mozwebqa.base_url:
            return PersonaServerHome(mozwebqa)
        elif 'anosrep.org' in mozwebqa.base_url:
            return PersonaServerHome(mozwebqa)
        else:
            raise UnknownHomePageException(
                "%s is not a known base_url" % mozwebqa.base_url)

    def click_sign_in(self):
        self.selenium.find_element(self._sign_in_locator).click()
        return SignIn(mozwebqa)

    def click_sign_out(self):
        self.selenium.find_element(self._sign_out_locator).click()
        # wait for something

    def click_sign_up(self):
        self.selenium.find_element(self._sign_in_locator).click()
        return SignIn(mozwebqa)

    @property
    def signed_in(self):
        pass

    @property
    def signed_in_user(self):
        return self.selenium.find_element(self._signed_in_user_locator).text

class OneTwoThreeDoneHome(HomePage):
    _sign_in_locator = ()
    _sign_out_locator = ()
    _sign_up_locator = ()
    _signed_in_user_locator = ()

    pass

class MyFavoriteBeerHome(HomePage):
    _sign_in_locator = ()
    _sign_out_locator = ()
    _sign_up_locator = ()
    _signed_in_user_locator = ()
    pass

class PersonaServerHome(HomePage):
    _sign_in_locator = ()
    _sign_out_locator = ()
    _sign_up_locator = ()
    _signed_in_user_locator = ()

    def click_sign_in(self):
        self.selenium.find_element(self._sign_in_locator).click()
        return ServerSignIn(mozwebqa)

    def click_sign_up(self):
        self.selenium.find_element(self._sign_in_locator).click()
        return ServerSignIn(mozwebqa)

    @property
    def signed_in(self):
        pass

    @property
    def signed_in_user(self):
        # persona server does not specify logged in user
        return self.signed_in


class UnknownHomePageException(Exception):
    def __init__(self, msg):
        self.msg = msg


class UnimplementedMethodError(Exception):
    def __init__(self, msg):
        self.msg = msg
