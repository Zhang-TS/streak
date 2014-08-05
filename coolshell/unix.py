#! /usr/bin/python

e = "abcdefghijklmnopqrstuvwxyz"
o = "pvwdgazxubqfsnrhocitlkeymj"

i = "Jktpt gktpt hv c vktss, gktpt hv c rcz. V tlutjg zey yvt gkt vktss jeffcaq ge vesxt gkhv upeistf, aer, ustcvt gpz yvham gkt peg13 en \"vktss\" ge tagtp atlg stxts."

result = ""

for n in i:
	key = o.find(n)
	if not key == -1:
		result += e[key]
	else:
		result += n

print result
