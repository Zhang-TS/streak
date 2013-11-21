#! /usr/bin/env python

"""
Day2: implementation of some soring algorithms
"""

"""
Insertion Sort:
A simple sorting algorithm, a comparison sort in which the sorted array is built one entry at a time. Most humans when sorting - ordering a deck of cards, for example-use a method that is similar to inserting sort.

Every repetition of insertion sort removes an element from the input data, inserting it into the correct position in the already-sorted list, until no input elements remain. The choice of which element to remove from the input is arbitrary, and can be made using almost any choice algorithm.

pseudocode:
for j <- 1 to length(A)-1
	key <- A[j]
	i <- j - 1
	while i >= 0 and A[i] > key
		A[i+1] <- A[i]
		i <- i - 1
	A[i+1] <- key
"""
def insertion_sort(A):
	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A

"""
Bubble sort:


A = [3,6,2,8,12,4,88,3,1,9]
sort = insertion_sort(A)
print sort
