#! /usr/bin/env python

"""
day4: continue with some sorting algorithm
"""

"""
quick-sort:a divide-and-conquer algorithm. It first divides a large list into two smaller sub-lists, the low elements and the high elements.
1. pick an element, called a pivot, from the list
2. reorder the list so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it(equal values can go either way). After this partitioning, the pivot is in its final position. This is called the partition operation
3. Recursively apply the above steps to the sub-list of elements with smaller values and separately the sub-list of elements with greater values

psudocode:

"""
#input list A, start index i, and end index j
def partition(A, i, j):
	# first element as the pivot	
	m = A[i]
	q = i
	for k in range(i,j+1):
		a = A[k]
		if A[k] < m:
			q += 1
			del(A[k])
			A.insert(i, a)
	return q

def quick_sort(A, i, j):
	size = j - i + 1;
	q = partition(A, i, j)
	if q-i > 1:
		quick_sort(A, i, q)
	if j-q > 1:
		quick_sort(A, q+1, j)


#using list comprehensions:
def qsort(list):
	if not list:
		return []
	else:
		pivot = list[0]
		less = [x for x in list if x < pivot]
		more = [x for x in list[1:] if x >= pivot]
		return qsort(less) + [pivot] + qsort(more)

unsort = [3, 4, 5, 23, 57, 1, 89, 63, 32, 83, 99]
#quick_sort(unsort,0, len(unsort)-1)
sort = qsort(unsort)
print sort

