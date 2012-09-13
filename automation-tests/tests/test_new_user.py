#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import time

from base import BaseTest
from pages.home import HomePage

@pytest.mark.mfb
@pytest.mark.persona
class TestNewUser(BaseTest):

    def test_new_primary_user_unauthenticated(self, mozwebqa):
        user = self.create_eyedee_user(mozwebqa, registered=False)
        homepage = HomePage(mozwebqa).factory()
        homepage.open_page()
        signin = homepage.click_sign_up()
        signin.email = user.primary_email
        signin.click_next(expect='idp')
        eyedee = signin.click_sign_in_with_primary()
        eyedee.new_password = user.password
        eyedee.click_create_account()

        assert homepage.is_the_current_page
        assert homepage.signed_in_user(user) == user.primary_email
        

    def test_new_primary_user_authenticated(self, mozwebqa):
        user = self.create_eyedee_user(mozwebqa, registered=True)
        homepage = HomePage(mozwebqa).factory()
        homepage.open_page()
        signin = homepage.click_sign_up()
        signin.email = user.primary_email
        signin.click_next(expect='popup_self_close')

        assert homepage.is_the_current_page
        assert homepage.signed_in_user(user) == user.primary_email

    @pytest.mark.skip_selenium
    def test_new_secondary_user_authenticated(self, mozwebqa):
        # take from 123done.tests.test_new_user::test_can_create_new_user_account
        pass

    @pytest.mark.skip_selenium
    def test_new_secondary_user_unauthenticated(self, mozwebqa):
        pass