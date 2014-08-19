#! /usr/bin/python

d = "abcdefghijklmnopqrstuvwxyz"
e = "pvwdgazxubqfsnrhocitlkeymj"

i="Wxgcg txgcg ui p ixgff, txgcg ui p epm. I gyhgwt mrl lig txg ixgff wrsspnd tr irfkg txui hcrvfgs, nre, hfgpig tcm liunz txg crt13 ra \"ixgff\" tr gntgc ngyt fgkgf."

result = ""

for n in i:
	key = e.find(n)
	if not key == -1:
		result += d[key]
	else:
		result += n

print result
