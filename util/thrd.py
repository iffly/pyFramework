#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread


def newThrd(handler, argv):
    try:
        thread.start_new_thread(handler, argv)
    except:
        print 'Failed to start thread'


def waitMain():
    while 1:
        pass
