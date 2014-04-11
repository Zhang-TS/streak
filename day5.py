#! /usr/bin/env python
import urllib2
import httplib

"""
python challenge puzzle
day5
day6
"""
def q1_power():
	return 2**38

print q1_power()

def q2_encryption(input):
	output = ""
	for c in input:
		if c.isalpha():
			s = ord(c)+2
			if s > ord('z'):
				s = s -26
			c = chr(s)
		output+=c
	return output

l = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
url = 'map'

print q2_encryption(url)

def q3_recognize_c():
	response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
	page_source = response.read()
	page_source = page_source.split('<!--')[2]
	s = ""
	for c in page_source:
		if c.isalpha():
			s += c
	print s

print q3_recognize_c()

def exactly(s):
	if s[0].islower() and s[8].islower() and s[1:4].isupper() and s[5:8].isupper() and s[4].islower():
		return True
	else:
		return False

def check_url(s):
	#s = s.lower()
	url = "www.pythonchallenge.com"
	path = "/pc/def/"+s+".html"
	try:
		conn = httplib.HTTPConnection(url)
		conn.request("HEAD", path)
		if conn.getresponse().status == 200:
			print s
	except StandardError:
		pass	
	
def q4_small_letter():
	response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
	page_source = response.read()
	page_source = page_source.split('<!--')[1]
	s = page_source[0:9]
	slist=[]
	for c in page_source[9:]:
		if not c.isalpha():
			continue
		if exactly(s):
			if s not in slist:
				slist.append(s)
				#check_url(s)
				print s
		s = s[1:]
		s += c

def check_url_2(url, params, method="GET"):
	if method == "POST":
		return urllib2.urlopen(url, data=urllib.urlencode(params))
	else:
		print "get "+url+"?"+urllib.urlencode(params)
		return urllib2.urlopen(url + "?" + urllib.urlencode(params))


def q5_linkedlist():
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
	number ="25357"

	while number.isdigit():

		params = {"nothing":number}
		response = check_url_2(url,params)
		f = response.read()

		print f

		for s in f.split():
			if s.isdigit():
				number = s
				print "number :" + number

	'''
	print "final number: " + number
	
	n = 16044
	while n > 0:
		n = n/2
		number = str(n)

		params = {"nothing":number}
		response = check_url_2(url, params)

		print response.read()
	'''

	'''
	hints: finally get 66831!
	'''

def q6_peak():
	try:
		with open('./banner.p', 'r') as rfile:
			result = pickle.load(rfile)

	except IOError as ioerr:
		print ioerr

	print len(result)

	for c in result:
		s = []
		for k in c:
			s.append(k[1])
		
		print s

q6_peak()
