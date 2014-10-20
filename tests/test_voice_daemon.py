#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of easyNav-pi-voice.
# https://github.com/easyNav/easyNav-pi-voice

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Joel Tong me@joeltong.org

from preggy import expect
import logging
import time

from easyNav_pi_dispatcher import DispatcherClient
from easyNav_pi_voice import VoiceDaemon
from tests.base import TestCase


class VoiceDaemonTestCase(TestCase):
    def test_can_run(self):
        """To run this test, ensure that dispatcher server is running. 
        Else will hang.
        """
        # expect(__version__).to_equal("0.1.0")
        d = VoiceDaemon()
        d.start()
        time.sleep(3)
        d.stop()


    def test_can_communicate(self):
        d = VoiceDaemon()
        d.start()
        time.sleep(3)

        # send test stuff
        sender = DispatcherClient(port=9001)
        sender.start()
        ## Dependency injection here
        sender.send(d.VOICE_DAEMON_ADDR, 'onData', {"count" : "counting numbers"})
        logging.info('finished sending.')
        sender.stop()

        # stop daemon
        d.stop()

