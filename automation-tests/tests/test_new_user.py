#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from base import BaseTest

# test cases not supported for myfavoritebeer
@pytest.mark.persona
class TestNewUser(BaseTest):
    
    def test_new_primary_user(mozwebqa):
        pass

    def test_new_secondary_user(mozwebqa):
        # take from 123done.tests.test_new_user::test_can_create_new_user_account
        pass