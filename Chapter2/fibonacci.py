#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:09:16 2017

@author: cavin
"""

def lib(n):
    a, b = 0, 1
    count = 1
    while count < n:
        a, b = b, a + b
        count = count + 1
    print(a)
    
def hanoi(a, b, c, n):
    if n == 1:
        print(a, '->', c)
    else:
        hanoi(a, c, b, n-1)
        print(b, '->', c)
        hanoi(b, a, c, n-1)
        
def foo(num, base):
    if (num >= base):
        foo(num // base, base)
    print(num % base, end = ' ')