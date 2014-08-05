#! /usr/bin/python

e = "-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?"

o = "[]',.pyfgcrl/=\\aoeuidhtns-;qjkxbmwvz{}\"<>PYFGCRL?+|AOEUIDHTNS_:QJKXBMWVZ"

inp = "macb() ? lpcbyu(&gbcq/_\\021%ocq\\012\\0_=w(gbcq)/_dak._=}_ugb_[0q60)s+"
result = ""
for n in inp:
	key = o.find(n)
	if not key == -1:
		result += e[key]
	else:
		result += n

with open("key.c", "w") as textfile:
	textfile.write(result)

print result
		


