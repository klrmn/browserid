#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from base import BaseTest


# tests not supported for myfavoritebeer
class TestVerification(BaseTest):
    
    # not applicable for persona server
    @pytest.mark.skip_selenium
    def test_verify_on_same_browser_should_redirect_to_client_site(self, mozwebqa):
        # use self.create_restmail_user()
        pass

    @pytest.mark.skip_selenium
    def test_verify_on_different_browser_should_ask_for_password_and_redirect_to_persona_server(self, mozwebqa):
        # use self.create_personatestuser_user(verified=False)
        pass

    @pytest.mark.skip_selenium
    @pytest.mark.persona
    @pytest.mark.not_123done
    @pytest.mark.xfail(reason="#2465 #2424")
    def test_verify_on_persona_server_should_redirect_to_management_page(self, mozwebqa):
        # use self.create_restmail_user()
        pass

    def test_verify_link_should_expire(self, mozwebqa):
        pytest.skip(reason="too long for an automated test")

