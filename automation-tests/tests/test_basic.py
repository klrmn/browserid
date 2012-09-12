#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from base import BaseTest

@pytest.mark.skip_selenium
class TestBasic(BaseTest):

    def github_is_available(self, mozwebqa):
        pass

    def restmail_is_available(self, mozwebqa):
        pass

    def eyedee_is_available(self, mozwebqa):
        pass

    def personatestuser_is_available(self, mozwebqa):
        pass
        
    def persona_server_is_available(self, mozwebqa):
        pass

    def client_site_is_available(self, mozwebqa):
        pass
    
