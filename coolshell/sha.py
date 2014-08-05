#! /usr/bin/python 
import hashlib

r = "e48d316ed573d3273931e19f9ac9f9e6039a4242"

i = "zWp8LGn01wxJ7"
code =[]


with open("./nqueen_result.txt", "r") as rfile:
	for l in rfile.readlines():
		code.append(l)

for s in code:
	h = hashlib.sha1(i+s).hexdigest()
	print h
	if h == r:
		print s


