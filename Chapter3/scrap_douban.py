#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 09:41:42 2017

@author: cavin
"""

import requests
from bs4 import BeautifulSoup as bs
import re

sum = 0
r = requests.get('https://book.douban.com/subject/20443559/')
soup = bs(r.text, 'lxml')
pattern = soup.find_all('p', 'comment-content')
for item in pattern:
    print(item.string)
    
pattern_s = re.compile('<span class="user-starts allstart10 rating">')
p = re.findall(pattern_s, r.text)
for star in p:
    sum += int(star)
print(sum)