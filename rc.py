#!/usr/bin/env python 


class RC(object):
    def __init__(self, rc, msg=''):
        self.rc = rc
        self.msg = msg

    def __eq__(self, x):
        return self.rc == x

    def __ne__(self, x):
        return self.rc != x

    def __lt__(self, x):
        return self.rc < x

    def __le__(self, x):
        return self.rc <= x

    def __gt__(self, x):
        return self.rc > x

    def __ge__(self, x):
        return self.rc >= x

    def __nonzero__(self):
        return self.rc != 0

