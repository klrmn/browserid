#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from base import BaseTest
from pages.home import HomePage

# test cases not supported for myfavoritebeer
@pytest.mark.persona
class TestNewUser(BaseTest):
    
    def test_new_primary_user_unauthenticated(self, mozwebqa):
        homepage = HomePage(mozwebqa.selenium, mozwebqa.timeout)
        pass

    def test_new_primary_user_authenticated(self, mozwebqa):
        pass

    def test_new_secondary_user(self, mozwebqa):
        # take from 123done.tests.test_new_user::test_can_create_new_user_account
        pass