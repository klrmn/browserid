#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest


class BaseTest(object):

    def create_personatestuser_user(self, mozwebqa, verified=True, env=None):
        '''Create a verified secondary user on personatestuser.org, and returns it.
        Use this method if you do not need to access additional emails later.
        Use this method if you do not want to be logged on as a precondition.
        '''
        from browserid import BrowserID
        bidpom = BrowserID(mozwebqa.selenium, mozwebqa.timeout)
        if 'dev' in mozwebqa.base_url:
            env = 'dev'
        elif 'anosrep' in mozwebqa.base_url:
            env = 'stage'
        else:
            env = 'prod'
        user = bidpom.persona_test_user(env=env, verified=verified)
        print user  # for debugging purposes
        return user

    def create_eyedee_user(self, mozwebqa, registered=True):
        '''Creates a primary user on eyedee.me and returns it.

        ::Args::
        - registered - if false, just generate email and password (default True)
        '''
        from browserid.mocks.user import MockUser
        user = MockUser(hostname='eyedee.me')
        if registered:
            from browserid.pages.eyedee import eyedee
            eyedee_page = eyedee(mozwebqa.selenium, mozwebqa.timeout)
            eyedee_page.create_user(user.id, user.password)

        print user  # for debugging purposes
        return user


    def create_restmail_user(self, mozwebqa, verified=True):
        '''Creates a verified secondary user using include.js and returns it.
        Use this method if you will need to access additional emails later.
        Use this method if you wish to be left logged in as a precondition.
        '''
        from browserid.mocks.user import MockUser
        user = MockUser()

        # create the user
        from pages.home import HomePage
        home = HomePage(mozwebqa)
        signup = home.click_sign_up()
        signup.sign_up(user.primary_email, user.password)

        if verified:
            # do email verification
            from browserid.pages.complete_registration import CompleteRegistration
            complete_registration = CompleteRegistration(mozwebqa.selenium, mozwebqa.timeout,
                self.get_confirm_url_from_email(user.primary_email),
                expect='redirect')

        print user  # for debugging purposes
        return user

    def clear_browser(self, mozwebqa):
        mozwebqa.selenium.execute_script('localStorage.clear()')

    def get_confirm_url_from_email(self, email, message_index=0):
        '''
        Checks the restmail inbox for the specified address
        and returns the confirm url.
        Specify message_count if you expect there to be more than one message for the user.
        Specify regex if you wish to use a specific regex. By default searches for a url with a 48 char token."
        '''

        from browserid.tests.restmail import RestmailInbox
        inbox = RestmailInbox(email)
        message = inbox.find_by_index(message_index)
        url = message.verify_user_link
        return url

    def confirm_email(self, mozwebqa, url, expect='redirect'):
        from browserid.pages.complete_registration import CompleteRegistration
        complete_registration = CompleteRegistration(mozwebqa.selenium, mozwebqa.timeout, url, expect=expect)
