#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from base import BaseTest

@pytest.mark.skip_selenium
class TestHealth(BaseTest):

    @pytest.mark.skip_selenium
    def test_github_is_available(self, mozwebqa):
        pass

    @pytest.mark.skip_selenium
    def test_restmail_is_available(self, mozwebqa):
        pass

    @pytest.mark.skip_selenium
    def test_eyedee_is_available(self, mozwebqa):
        pass

    @pytest.mark.skip_selenium
    def test_personatestuser_is_available(self, mozwebqa):
        pass
        
    @pytest.mark.skip_selenium
    def test_persona_server_is_available(self, mozwebqa):
        pass

    @pytest.mark.skip_selenium
    def test_client_site_is_available(self, mozwebqa):
        pass
    
