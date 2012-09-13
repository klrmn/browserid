#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import uuid


class MockUser(dict):

    def __init__(self, hostname='restmail.net', **kwargs):
        self['id'] = self._create_id()
        self['primary_email'] = '%s@%s' % (self.id, hostname)
        self['password'] = 'password'
        self['additional_emails'] = []

        self.update(**kwargs)

    def __getattr__(self, attr):
        return self[attr]

    def _create_id(self):
        return 'bidpom_%s' % uuid.uuid1()

    def add_email(hostname='restmail.net'):
        username = self._create_id()
        email = '%s@%s' % (username, hostname)
        self['additional_emails'].append(email)
        return email