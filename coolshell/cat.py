#! /usr/bin/python

import urllib
import urllib
import httplib
import re

#response = urllib.urlopen("http://fun.coolshell.cn/furyy.html")
#page_source = response.read()
#page_source = page_source.split('<!--')[1]
with open("./cat2_text.txt", "r") as rfile:
	page_source = rfile.read()

s = page_source[0:5]
slist = []

def exactly2(s):
	if s[0] == s[4] and s[1] == s[3]:
		return True
	else:
		return False	


def regular(s):
	m = re.search(r'[A-Z0-9][A-Z0-9][a-z][A-Z0-9][A-Z0-9]', s)
	if not m == None:
		return True
	else:	
		return False


def regular2(s):
	if s[0].isalpha() and s[1].isalpha():
		return False
	elif s[0].isdigit() and s[1].isdigit():
		return False

	print s
	return True

for c in page_source[5:]:
	if exactly2(s):
		slist.append(s)
	s = s[1:]
	s += c

for u in slist:
	if regular(u):
		regular2(u)
