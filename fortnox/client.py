#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy


class Fortnox(object):
    """
    Acts as the Client with Fortnox REST api
    """

    DEFAULT_OPTIONS = {
        "server": "https://api.fortnox.se/3/",
        "api_version": "3",
        "check_update": False,
        "headers": {
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/json',
        }
    }


    def __init__(self, server=None, options=None, oauth=None, logging=True):
        """
        Construct a Fortnox client instance.
        """

        if server:
            options['server'] = server

        self.logging = logging

        self._options = copy.copy(Fortnox.DEFAULT_OPTIONS)

        self._options.update(options)

        # TODO: Setup OAuth2 connection and check that we got a pulse
