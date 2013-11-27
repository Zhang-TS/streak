#! /usr/bin/env python

"""
python challenge puzzle
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

print q2_encryption('ocr')

def q3_recognize_c(input):
	s = 0
	for c in input:
		print ord(c)
		s += ord(c)
	print s

print q3_recognize_c('2')

