# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 19:51:03 2017

@author: Administrator
"""

import string

def countchar(str):
    str = str.lower()
    d = dict()
    for i in string.ascii_lowercase:
        d[i] = 0

    for i in str:
        if i in d:
            d[i] += 1

    value = [d[i] for i in sorted(d)]
    return value

if __name__ == "__main__":
    str = input()
    print(countchar(str))
