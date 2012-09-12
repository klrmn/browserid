#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from base import BaseTest

# add user cases not supported for myfavoritebeer
# add user cases not supported for persona server
class TestAddUser(BaseTest):
    
    _max_emails_per_user = 8  # issue #2399 PR #2422

    def test_add_primary_email_to_primary_based_account(self, mozwebqa):
        pass

    def test_add_primary_email_to_secondary_based_account(self, mozwebqa):
        pass

    def test_add_secondary_email_to_primary_based_account(self, mozwebqa):
        pass

    def test_add_secondary_email_to_secondary_based_account(self, mozwebqa):
        # take from browserid.tests.check_add_email::test_add_email
        pass

    def test_can_add_at_least_max_users(self, mozwebqa):
        pass

