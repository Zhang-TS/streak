#! /usr/bin/env python

'''
This is to solve a quiz:
two numbers in 2-99 range, one mathmatician (Mr. product) knows the product of the two numbers, and the other matchmatician (Mr. sum) knows the sum of the two numbers, they have the following conversations:

Mr. product: I don't know what x, y are
Mr. sum: I knew you don't know!
Mr. product: Now I know!
Mr. sum: well, I will know if you know.

What are the two numbers?
'''

#find the factors of the number, exclusive of 1 and itself
def factors(n):    
	s = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
	s.remove(1)
	s.remove(n)
	return list(s)


#find the sum_list of the number
def find_sum_list(n):
	s_l = []
	f = factors(n) #find factors of n
	for k in f:
		i = n /k
		if i < 100:
			if k > i:
					tmp = i
					i = k
					k = tmp
					s = (i+k, k, i)
					if s not in s_l:
						s_l.append(s)	
	return s_l

#check the sum is in possible list or not, and only one in possible list is 
#what we want! no more no less!!
def check_sum_in_p(sum_list):
	if len(sum_list) == 0 or len(sum_list) == 1:
		return False, ()

	s = [] #store the sum if sum in possible list
	for k in sum_list:
		if k[0] in p:
			s.append(k)

	if len(s) == 1: #if just one sum in possible list, this is we want
		#print s[0]	
		return True, s[0]
	else:
		return False, ()


prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
s =[]
#find the possible sum list
for k in prime:
	for b in prime:
		if not k == b and (k+b) not in s:
			s.append(k+b)
p =[]
for i in range(2,197):
	if i not in s:
		p.append(i)
print "possible list: "
print len(p)


#check all the possible multiplications between two number in 2-99
li = []
for i in range(2, 100):
	for j in range(2, 100):
		if not j == i:
			m = i*j
			s_list = find_sum_list(m)
			b, s = check_sum_in_p(s_list)
			
			if b:
				if s not in li:
					li.append(s)
print "sum list from possible multiplication: "
print len(li)
r = []
for k in li:
	r.append(k[0])

#find the occurance of element in r
oc = []
l = []
for k in r:
	if k not in l:
		l.append(k)
		oc.append(0)
	else:
		oc[l.index(k)] += 1

result = zip(l, oc)
for k in result:
	if k[1] == 0:
 		s = k[0]

#the final answer:
for k in li:
	if k[0] == s:
		print "the two numbers are : " , k[1:]
