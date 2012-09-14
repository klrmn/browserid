#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import time

from base import BaseTest
from pages.home import HomePage
from browserid.mocks.user import MockUser


class TestNewUser(BaseTest):

    @pytest.mark.mfb
    @pytest.mark.persona
    def test_new_primary_user_unauthenticated(self, mozwebqa):
        user = MockUser(hostname='eyedee.me')
        
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
        

    @pytest.mark.mfb
    @pytest.mark.persona
    def test_new_primary_user_authenticated(self, mozwebqa):
        user = self.create_eyedee_user(mozwebqa, authenticated=True)
        homepage = HomePage(mozwebqa).factory()
        homepage.open_page()
        signin = homepage.click_sign_up()
        signin.email = user.primary_email
        signin.click_next(expect='popup_self_close')

        assert homepage.is_the_current_page
        assert homepage.signed_in_user(user) == user.primary_email

    @pytest.mark.persona
    def test_new_secondary_user_redirects_to_rp(self, mozwebqa):
        # taken from 123done.tests.test_new_user::test_can_create_new_user_account
        if 'myfavoritebeer' in mozwebqa.base_url:
            pytest.skip("this test case does not run on mfb")
            return

        user = MockUser(hostname='restmail.net')
        homepage = HomePage(mozwebqa).factory()
        homepage.open_page()
        signin = homepage.click_sign_up()
        signin.email = user.primary_email
        signin.click_next(expect='verify')
        signin.password = user.password
        signin.verify_password = user.password
        signin.click_verify_email()
        signin.close_window()
        signin.switch_to_main_window()

        url = self.get_confirm_url_from_email(user.primary_email)
        self.confirm_email(mozwebqa, url, expect='redirect')

        assert homepage.is_the_current_page
        assert homepage.signed_in_user(user) == user.primary_email

    @pytest.mark.mfb
    def test_new_secondary_user_redirects_to_server(self, mozwebqa):

        if not 'myfavoritebeer' in mozwebqa.base_url:
            pytest.skip("this test only runs on mfb")
            return
            
        from browserid.mocks.user import MockUser
        user = MockUser(hostname='restmail.net')
        homepage = HomePage(mozwebqa).factory()
        homepage.open_page()
        signin = homepage.click_sign_up()
        signin.email = user.primary_email
        signin.click_next(expect='verify')
        signin.password = user.password
        signin.verify_password = user.password
        signin.click_verify_email()
        signin.close_window()
        signin.switch_to_main_window()

        url = self.get_confirm_url_from_email(user.primary_email)
        self.confirm_email(mozwebqa, url, expect='redirect')

        from pages.home import PersonaServerHome
        manage_page = PersonaServerHome(mozwebqa)

        assert manage_page.is_the_current_page
