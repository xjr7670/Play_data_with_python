#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 10:45:52 2017

@author: cavin
"""

import re
import requests
from bs4 import BeautifulSoup

url = "http://money.cnn.com/data/dow30/"
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'lxml')

codes = [c.text for c in soup.find_all("a", "wsod_symbol")]
names = [n.text for n in soup.find_all("span", title=True)]
prices = [float(p.text) for p in soup.find_all("span", class_="wsod_stream", stream=re.compile(r"last_\d+"))]
print(len(codes), len(names), len(prices))
total_list = list()
for i in range(0, 30):
    total_list.append((codes[i], names[i], prices[i]))
else:
    print(total_list)