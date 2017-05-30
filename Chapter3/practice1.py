# coding: utf8

import requests
from bs4 import BeautifulSoup
import re

def get_content(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')

    comment_list = list()
    comments = soup.find_all("p", "comment-content")
    for comment in comments:
        comment_list.append(comment.text)
    
    rate_list = list()
    rate_pat = re.compile(r"user-stars allstar(\d+) rating")
    rates = re.findall(rate_pat, html)
    for rate in rates:
        rate_list.append(int(rate))
    
    return (comment_list, rate_list) 

if __name__ == "__main__":
    comment_list = list()
    rate_list = list()
    l = len(comment_list)
    i = 1
    while l < 50:
        url = "https://book.douban.com/subject/26610864/comments/hot?p=%d" % i
        comments, rates = get_content(url)
        comment_list.extend(comments)
        rate_list.extend(rates)
        l = len(comment_list)
        i += 1
        
    print(comment_list, sum(rate_list)/50)
        