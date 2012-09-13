#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json
import time
import re
from time import sleep
import requests


def get_mail(username, message_count=1, timeout=60):
    username = username.partition('@restmail.net')[0]
    end_time = time.time() + timeout
    while(True):
        print 'getting email for %s' % username
        response = requests.get(
            'https://restmail.net/mail/%s' % username,
            verify=False)
        restmail = json.loads(response.content)
        if len(restmail) == message_count:
            print 'message found'
            return restmail
        time.sleep(0.5)
        if(time.time() > end_time):
            break
    raise Exception('Timeout after %(TIMEOUT)s seconds getting restmail for '
                    '%(USERNAME)s. Expected %(EXPECTED_MESSAGE_COUNT)s '
                    'messages but there were %(ACTUAL_MESSAGE_COUNT)s.' % {
                        'TIMEOUT': timeout,
                        'USERNAME': username,
                        'EXPECTED_MESSAGE_COUNT': message_count,
                        'ACTUAL_MESSAGE_COUNT': len(restmail)})


class RestmailInbox(object):
    """
    This wrapper loads restmail for the given email address.
    It will loop and wait for an email to arrive if there is not one present.
    find_by_* methods can be used to find an email and return it as Email() class.
    """

    _restmail_mail_server = "https://restmail.net/mail/"

    def __init__(self, email):
        self.email = email
        self.username = email.split('@')[0]
        self.json = self._wait_and_return_json_response(self.username)

    def _wait_and_return_json_response(self, username, timeout=60):
        # Loop for 60 attempts until the restmail json returned is not empty

        timer = 0
        response_json = []

        while timer < timeout:
            sleep(1)
            timer += 1

            response = requests.get(self._restmail_mail_server + self.username, verify=False)
            response_json = json.loads(response.content)
            if response_json != []:
                return response_json

        raise Exception("Failed to find an email before timeout")

    def delete_all_mail(self):
        # Delete all of the mail in the inbox

        requests.delete(self._restmail_mail_server + self.username, verify=False)

    def find_by_index(self, index):
        return Email(self.json[index])

    def find_by_sender(self, sender):
        # Loop through the address and name objects for each sender and match at least one

        for json_object in self.json:
            for from_source in json_object['from']:
                if from_source['address'] == sender or from_source['name'] == sender:
                    return Email(json_object)
        else:
            raise Exception("Sender not found")


class Email():
    """
    This returns a class representation of an email from restmail inbox
    """

    def __init__(self, json):
        self.json = json

    @property
    def body(self):
        return(self.json['text'])

    @property
    def confirm_link(self):
        regex = '(https?:.*?token=.{48})'
        confirm_link = re.search(regex, self.body).group(0)
        return confirm_link
        
    @property
    def verify_user_link(self):
        # This returns the link for verifying the email address of a new account
        regex = 'https:\/\/.*verify_email_address\?token=.{48}'

        verify_link = re.search(regex, self.body).group(0)
        return verify_link

    @property
    def add_email_address_link(self):
        # This returns the link for adding the email address of a new account
        regex = 'https:\/\/.*confirm\?token=.{48}'

        add_email_link = re.search(regex, self.body).group(0)
        return add_email_link
