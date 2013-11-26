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
		while i >= 0 and A[i] < key:
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A

"""
Bubble sort:
works by repeatedly stepping through the list to be sorted, comparing each pair of adjacent items and swapping them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. 
psudocode:
for i = 1:n
	swapped = false
	for j = n:i+1
		if a[j] < a[j-1]
			swap a[j, j-1]
			swapped = true
	break if not swapped
end
"""
def bubble_sort(A):
	while True:
		swap = False
		for i in range(1, len(A)):
			if A[i]	< A[i-1]:
				temp = A[i]
				A[i] = A[i-1]
				A[i-1] = temp
				swap = True
		if not swap:
			break


A = [3,6,2,8,12,4,88,3,1,9]
sort = insertion_sort(A)
bubble_sort(A)
print sort
print A
