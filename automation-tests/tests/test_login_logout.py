#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from base import BaseTest

# which of these should be supported by myfavoritebeer?
class TestLoginLogout(BaseTest):
    
    def test_sign_in_with_primary_address(self, mozwebqa):
        # any verification should be via IdP
        pass

    def test_sign_in_with_secondary_address(self, mozwebqa):
        # should require persona password
        pass

    def test_initial_login_in_browser(self, mozwebqa):
        # should require IdP / secondary authentication
        pass

    def test_second_login_within_60_sec(self, mozwebqa):
        # should not ask if it is your computer
        # take from browserid.tests.check_sign_in::test_sign_in_returning_user
        pass

    def test_second_login_after_60_sec(self, mozwebqa):
        # should be asked if it is your computer
        # take from browserid.tests.check_sign_in::test_sign_in_is_this_your_computer
        pass

    def test_this_is_my_computer(self, mozwebqa):
        # next login should not require password
        pass

    def test_this_is_not_my_computer(self, mozwebqa):
        # next login should require password
        pass

    def test_logout_from_client_site(self, mozwebqa):
        # should log out
        # should not cause logout from any other client site
        # should not cause logout from persona server
        pass

    @pytest.mark.???
    def test_logout_from_persona_server(self, mozwebqa):
        # should log out
        # should cause logout from all client sites
        pass