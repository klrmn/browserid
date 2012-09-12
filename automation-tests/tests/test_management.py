#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from base import BaseTest


# tests not supported for myfavoritebeer
class TestManagement(BaseTest):
    
    @pytest.mark.persona
    @pytest.mark.not_123done
    def test_primary_user_cannot_change_password(self, mozwebqa):
        pass

    @pytest.mark.persona
    @pytest.mark.not_123done
    def test_secondary_user_can_change_password(self, mozwebqa):
        # take from persona_server.tests.test_manage_account::test_that_user_can_change_password
        pass

    @pytest.mark.persona
    def test_secondary_user_can_forgot_password(self, mozwebqa):
        # take from persona_server.tests.test_manage_account::test_that_user_can_reset_password
        pass

    @pytest.mark.persona
    def test_primary_user_cannot_forget_password(self, mozwebqa):
        pass

    @pytest.mark.persona
    @pytest.mark.not_123done
    def test_primary_user_can_cancel_account(self, mozwebqa):
        pass

    @pytest.mark.persona
    @pytest.mark.not_123done
    def test_secondary_user_can_cancel_account(self, mozwebqa):
        # take from persona_server.tests.test_manage_account::test_that_user_can_cancel_account_with_one_email
        pass

    @pytest.mark.???
    def test_primary_email_can_be_removed_from_account(self, mozwebqa):
        pass

    @pytest.mark.???
    def test_secondary_email_can_be_removed_from_account(self, mozwebqa):
        pass
