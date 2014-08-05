#! /usr/bin/python

alp = "abcdefghijklmnopqrstuvwxyz"

a = "duyo"
b = "aa"

size = len(a)
s = 0
for i in a:
	index = alp.find(i)+1
	s += index*26**(size-1)
	size -= 1

print s		

size = len(b)
s1 = 0
for i in b:
	index = alp.find(i)+1
	s1 += index*26**(size-1)
	size -= 1

print s/s1
