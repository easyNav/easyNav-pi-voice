Voice Daemon
=====================================

## What is it?

Voice Daemon for easyNav. 


## Installation

	$ sudo pip install .


## Running Voice Daemon

Installation via pip ensures daemon is installed locally.  To run, execute:

	$ easyNav-pi-voice


## Running tests

Voice Daemon uses `make`.  To run, execute:

	$ make test


## Development 

	Voice module consists of event handlers via `attachEvent()`, a `tick()` function handler.  Edit these accordingly.  

	Don't forget the dependencies!  Remember to bump the version number if doing newer installation.
