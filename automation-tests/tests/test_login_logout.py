#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from base import BaseTest
from pages.home import HomePage

# which of these should be supported by myfavoritebeer?
class TestLoginLogout(BaseTest):
    
    @pytest.mark.persona_server
    @pytest.mark.mfb
    def test_sign_in_and_out_with_primary_address_authenticated(self, mozwebqa):
        user = self.create_eyedee_user(mozwebqa, authenticated=True)

        homepage = HomePage(mozwebqa).factory()
        homepage.open_page()
        signin = homepage.click_sign_in()
        signin.email = user.primary_email
        signin.click_next(expect='popup_self_close')

        assert homepage.is_the_current_page
        assert homepage.signed_in_user(user) == user.primary_email

        homepage.click_sign_out()
        assert homepage.signed_out

    @pytest.mark.persona_server
    @pytest.mark.mfb
    def test_sign_in_and_out_with_primary_address_unauthenticated(self, mozwebqa):
        user = self.create_eyedee_user(mozwebqa, authenticated=False)

        homepage = HomePage(mozwebqa).factory()
        homepage.open_page()
        signin = homepage.click_sign_in()
        signin.email = user.primary_email
        signin.click_next(expect='idp')
        eyedee = signin.click_sign_in_with_primary()
        eyedee.password = user.password
        eyedee.click_sign_in()

        assert homepage.is_the_current_page
        assert homepage.signed_in_user(user) == user.primary_email

        homepage.click_sign_out()
        assert homepage.signed_out

    # not logical for persona server, as that's the only place to get an 
    # authenticated secondary user
    @pytest.mark.mfb
    def test_sign_in_and_out_with_secondary_address_authenticated(self, mozwebqa):
        if 'persona' in mozwebqa.base_url or 'anosrep' in mozwebqa.base_url:
            pytest.skip("this test is illogical for the persona server")
            return
            
        user = self.create_persona_user(mozwebqa, verified=True)

        homepage = HomePage(mozwebqa).factory()
        homepage.open_page()
        signin = homepage.click_sign_in(expect='returning')
        signin.click_sign_in_returning_user(expect='login')

        assert homepage.is_the_current_page
        assert homepage.signed_in_user(user) == user.primary_email

        homepage.click_sign_out()
        assert homepage.signed_out

    @pytest.mark.persona_server
    @pytest.mark.mfb
    def test_sign_in_and_out_with_secondary_address_unauthenticated(self, mozwebqa):
        user = self.create_personatestuser_user(mozwebqa, verified=True)

        homepage = HomePage(mozwebqa).factory()
        homepage.open_page()
        signin = homepage.click_sign_in()
        signin.email = user.primary_email
        signin.click_next(expect='password')
        signin.password = user.password
        signin.click_sign_in()

        assert homepage.is_the_current_page
        assert homepage.signed_in_user(user) == user.primary_email

        homepage.click_sign_out()
        assert homepage.signed_out

    @pytest.mark.skip_selenium
    def test_initial_login_in_browser(self, mozwebqa):
        # should require IdP / secondary authentication
        pass

    @pytest.mark.skip_selenium
    def test_second_login_within_60_sec(self, mozwebqa):
        # should not ask if it is your computer
        # take from browserid.tests.check_sign_in::test_sign_in_returning_user
        pass

    @pytest.mark.skip_selenium
    def test_second_login_after_60_sec(self, mozwebqa):
        # should be asked if it is your computer
        # take from browserid.tests.check_sign_in::test_sign_in_is_this_your_computer
        pass

    @pytest.mark.skip_selenium
    def test_login_email_picker(self, mozwebqa):
        pass
        
    @pytest.mark.skip_selenium
    def test_this_is_my_computer(self, mozwebqa):
        # next login should not require password
        pass

    @pytest.mark.skip_selenium
    def test_this_is_not_my_computer(self, mozwebqa):
        # next login should require password
        pass

    @pytest.mark.skip_selenium
    def test_logout_from_client_site(self, mozwebqa):
        # should log out
        # should not cause logout from any other client site
        # should not cause logout from persona server
        pass

    # @pytest.mark.???
    @pytest.mark.skip_selenium
    def test_logout_from_persona_server(self, mozwebqa):
        # should log out
        # should cause logout from all client sites
        pass