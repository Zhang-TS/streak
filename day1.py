#! /usr/bin/env python

"""
Consider the following picture:
            _ _
           |7 7|_
  _        |    6|
 |5|      _|     |
 | |    _|4      |
_| |  _|3        |
2  |_|2          |
____1____________|
0 1 2 3 4 5 6 7 8

In this picture we have walls of different heights, This picture is represented by an array of integers, where the value at each index is the height of the wall. The picture above is represented with an array as [2,5,1,2,3,4,7,7,6].

Now imagine it rains, How much water is going to be accumulated in puddles between walls?

"""

#find how many compartment is formed by the wall, by checking the first highest point, followed by the first highest point/global highest point in the rest of the wall
#return two lists: one to store the start point index and one to store the end point index
def find_compartment(wall):
	size = len(wall)
	start = False
	start_index = []
	end_index = []
	i = 1;

	while(True):
		if i >= size:
			break
		#check local highest to start
		if not start:
			if wall[i] >= wall[i-1]:
				i += 1	
				continue
			else:
				ref_level = wall[i-1]
				start = True;
				#save the start index
				start_index.append(i-1)
				continue
		
		#decide the end index
		max_index = find_max(wall, ref_level, i, size-1)
		if max_index == -1:
			del start_index[-1]
			break
		i = max_index+1
		end_index.append(max_index)
		start = False
		continue
	
	print start_index
	print end_index	
	return start_index, end_index

#find the global maximum/the first point that exceeds the ref level, giving the list and the start and end point
#check if it descends all the way to the end, then will not form a compartment
def find_max(wall, ref_level, start, end):
	decline = True
	m = wall[start]
	index_max = start
	for i in range(start+1, end):
		if wall[i] > wall[i-1]:
			decline = False
		if wall[i] > ref_level:
			m = wall[i]
			index_max = i
			break
		if wall[i] > m:
			m = wall[i]
			index_max = i
	if decline:
		return -1
	else:
		return index_max

#find the area giving the wall and the start and end point
def find_area(wall, start, end):
	if wall[start] > wall[end]:
		lowest = wall[end]
	else:
		lowest = wall[start]

	area = (end-start-1)*lowest
	for w in wall[start+1:end]:
		area = area - w

	return area

wall = [3,1,2,1,5,3,6,1,2,1,4,1,3,2,1,3,2]
start_index, end_index = find_compartment(wall)
area = 0
for i,j in zip(start_index, end_index):
	area += find_area(wall, i, j)

print area
