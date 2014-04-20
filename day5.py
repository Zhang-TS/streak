#! /usr/bin/env python

import urllib2
import urllib
import httplib
import pickle
from PIL import Image
import numpy as np
import zipfile
import os.path
import bz2
import matplotlib.pyplot as plt

def q3_orc():
	response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
	page_source = response.read()
	page_source = page_source.split('<!--')[2]

	cha =[]
	idx =[]
	for c in page_source:
		if c not in cha:
			cha.append(c)
			idx.append(1)
		else:
			idx[cha.index(c)] += 1

	result = zip(cha, idx)

	print result

def q4_equality():
	response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
	page_source = response.read()
	page_source = page_source.split('<!--')[1]

	s = page_source[0:9]
	slist = []
	for c in page_source[9:]:
		if not c.isalpha():
			continue
		if exactly(s):
			if s not in slist:
				slist.append(s)
		s = s[1:]
		s += c
	url = ''
	for c in slist:
		url += c[4]

	check_url(url)

	print slist

def exactly(s):
	if s[0].islower() and s[8].islower() and s[1:4].isupper() and s[5:8].isupper() and s[4].islower():
		return True
	else:
		return False

def check_url(s):
	print s
	url="www.pythonchallenge.com"
	path="/pc/def/"+s+".html"

	print path

	try:
		conn = httplib.HTTPConnection(url)
		conn.request("HEAD", path)
		if conn.getresponse().status == 200:
			print "ok"
			return True
	except StandardError:
		pass

	return False

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
		s = ""
		for k in c:
			if k[0] == " ":
				for i in range(k[1]):
					s += " "
			else:
				for i in range(k[1]):
					s += "#"
		
		print s


def q7_channel():
	zip_file = zipfile.ZipFile(open('./channel.zip', 'r'))


	nothing = '90052'
	comments = []
	while True:
		if os.path.isfile(os.path.join('./channel/', nothing+'.txt')):
			raw_data = zip_file.read(nothing+'.txt')

			print raw_data

			comments.append(zip_file.getinfo(nothing+'.txt').comment)
			nothing = raw_data.split()[-1]
		else:
			break

	print "".join(comments)



def q8_oxygen():
	img = Image.open('./oxygen.png').convert('L')

	width, height = img.size

	mid_h = height/2

	img_data = np.asarray(img, dtype=int)

	row = img_data[mid_h, 0:width-21].tolist()

	row.insert(0, 115)
	row.insert(0, 115)
	
	s = ""
	for k in range(0, width-21, 7):
		s += (chr(row[k]))

	s1 = s.split("[")[1]
	s2 = s1.split("]")[0]

	print s2

	result =""
	for k in s2.split(","):
		result += chr(int(k))

	print result

def q9_integrity():
	name = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
	pas = "BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"

	print bz2.decompress(name)
	print bz2.decompress(pas)

def q10_good():
	url = "http://www.pythonchallenge.com/pc/return/good.html"
	username='huge'
	password='file'
	p = urllib2.HTTPPasswordMgrWithDefaultRealm()

	p.add_password(None, url, username, password)

	handler = urllib2.HTTPBasicAuthHandler(p)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)

	response = urllib2.urlopen(url)
	page_source = response.read()
	page_source = page_source.split('first:')[1]

	page_source = page_source.split('second:')
	first = page_source[0]
	second = page_source[1]

	#store the numbers
	first_list = []	
	for k in first.split():
		for n in k.split(','):
			if n.isdigit():
				first_list.append(int(n))

	second_list = []	
	for k in second.split():
		for n in k.split(','):
			if n.isdigit():
				second_list.append(int(n))
	pos = work_with_number(second_list)
	connect_dot(pos)

def work_with_number(l):
	l1 = [l[k] for k in range(0, len(l), 2)]
	l2 = [l[k] for k in range(1, len(l), 2)]

	pos = zip(l1, l2)
	return pos

def connect_dot(t):
	fig = plt.figure()
	x, y = zip(*t)
	i0 = x[0]
	j0 = y[0]
	for i, j in t:
		plt.plot([i0,i], [j0, j])
		i0 = i
		j0 = j
	
	plt.show()	
q10_good()

