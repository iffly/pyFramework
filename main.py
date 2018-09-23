#!/usr/bin/python
# -*- coding: UTF-8 -*-

from util.thrd import newThrd
from util.thrd import waitMain


def hello(s):
    print s


if __name__ == '__main__':
    newThrd(hello, ('hello',))

    waitMain()
