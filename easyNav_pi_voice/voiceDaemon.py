#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of easyNav-pi-voice.
# https://github.com/easyNav/easyNav-pi-voice

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Joel Tong me@joeltong.org

import logging
import threading
import smokesignal

from easyNav_pi_dispatcher import DispatcherClient


class VoiceDaemon:
    """ The Voice Daemon is the voice component for easyNav.  
    Example Code:

    daemon = VoiceDaemon()
    daemon.start() # Starts the daemon 
    daemon.stop() # Stops the daemon 
    """
    def __init__(self):
        """Initializes the daemon.
        """
        self.VOICE_DAEMON_ADDR = 9010
        self._active = False
        self._dispatcherClient = DispatcherClient(port=self.VOICE_DAEMON_ADDR)
        self._attachHandlers() ## Attach event handlers here
        ### Start declare variables here  ###
        ###
        ###
        ### End declare variables here    ###
        logging.info('Voice Daemon instantiated.')


    def start(self):
        """Starts the daemon.
        """
        self._active = True

        ## Run tick thread
        def runThread():
            while(self._active):
                self._tick()

        self._threadListen = threading.Thread(target=runThread)
        self._dispatcherClient.start() # start comms
        self._threadListen.start()
        logging.info('Voice Daemon: Thread started.')


    def stop(self):
        self._dispatcherClient.stop() # Stop comms
        self._active = False
        self._threadListen.join()
        ### Start De-initialize variables here  ###
        ###
        ###
        ### End De-initialize variables here    ###
        logging.info('Serial Daemon: Thread stopped.')


    def _tick(self):
        """Tick function run when daemon is active 
        """
        #########################################
        #             <<FILL IN>>               #
        #########################################
        pass


    def _attachHandlers(self):
        """Attach event handlers here
        """
        ###################################################
        #######     Define event handlers here      #######
        ###################################################

        #########################################
        #             <<FILL IN>>               #
        #########################################

        ### Sample handler
        @smokesignal.on('onData')
        def onDataHandler(messageObj):
            """ Event callback for serial data 
            """
            logging.debug('Oh yay!  I got triggered!')
            pass

        ###################################################
        #######   End Define event handlers here    #######
        ###################################################




###################################
##  Main program defined here    ##
###################################

def runMain():
    """ Main function called when run as standalone daemon
    """
    def configLogging():
        logging.getLogger('').handlers = []
        logging.basicConfig(
            # filename = "a.log",
            # filemode="w",
            level = logging.DEBUG)

    ## Run the stuff here ##
    configLogging()
    daemon = VoiceDaemon()
    daemon.start()


if __name__ == '__main__':
    runMain()
