__author__ = 'Owner'
import string


def canaccept(s):
    a = str(s)
    if a.startswith('mailto:'):
        return True
    return False


def fix(s):
    a = str(s)
    return string.replace(a, 'mailto:', '')

