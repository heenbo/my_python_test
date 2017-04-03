#!/usr/bin/python2

#coding=utf8

import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://tieba.baidu.com/")

print(html)
