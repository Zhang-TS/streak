#! /usr/bin/env python

"""
Day3: continue with some sorting algorithm
"""

"""
Merge sort:
The merge sort algorithm closely follows the divide-and-conquer paradigm. 
Divide: devide the n-element sequence to be sorted into two subsequences of n/2 elements each
Conquer: sort the two subsequences recursively using merge sort
Combine: merge the two sorted subsequences to produce the sorted answer

psudocode for MERGE
MERGE(A, p, q, r)
	n1 = q-p+1
	n2 = r-q
	let L[1...n1+1] and R[1..n2+1] be new arrays
	for i = 1 to n1
		L[i] = A[p+i-1]
	for j = 1 to n2
		R[j] = A[q+j]
	L[n1+1] = inf
	R[n2+1] = inf
	i = 1
	j = 1
	for k = p to r
		if L[i]<= R[j]	
			A[k] = L[i]
			i = i + 1
		else
			A[k] = R[j]
			j = j + 1

psudocode for MERGE-SORT
MERGE-SORT(A, p, r)
	if p < r
		q = floor((p+r)/2)
		MERGE-SORT(A, p, q)
		MERGE-SORT(A, q+1, r)
		MERGE(A,p,q,r)

"""

def merge(A, p, q, r):
	n1 = q-p+1
	n2 = r-q
	L = []
	R = []
	for i in range(1, n1+1):
			L.append(A[p+i-1])
	for j in range(1, n2+1):
			R.append(A[q+j])
	L.append(1000000)
	R.append(1000000)
	i = 0
	j = 0
	for k in range(p, r+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1
	return A

def merge_sort(A, p, r):
	if p < r:
		q = (p+r)/2
		A = merge_sort(A, p, q)
		A = merge_sort(A, q+1, r)
		A = merge(A, p, q, r)

	return A

#test merge
A = [1,6,8,10,2,3,5,7]
sort_A = merge_sort(A, 0, 7)
print sort_A

