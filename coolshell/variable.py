#! /usr/bin/python
import urllib2

def check_url_2(url, params, method="GET"):
	if method == "POST":
		return urllib2.urlopen(url, data=urllib.urlencode(params))
	else:
		print "get "+url+"?"+urllib.urlencode(params)
		return urllib2.urlopen(url + "?" + urllib.urlencode(params))

path = "http://fun.coolshell.cn/n/"
s = " 13310"
while s is not None:
	res = urllib2.urlopen(path + s)
	s = res.read()
	print s

