'''
This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.

Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.

The numeric answer for the given input file should be typed in the space below.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.

(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)

[TIP: before submitting, first test the correctness of your program on some small test files or your own devising. Then post your best test cases to the discussion forums to help your fellow students!]

developer - Denis Kotov
'''

file = open("IntegerArray.txt", 'r')
numbers = []
for line in file:
	numbers.append(int(line))

def print_array(num):
	for n in num:
		print(str(n))
	
def CountInvertion(array):
	if len(array) == 1:
		return (array, 0)
	else:
		half = int(len(array)/2)
		sorted_x, x = CountInvertion(array[0:half]) 
		sorted_y, y = CountInvertion(array[half:])
		sorted_z, z = CountSplitInvertion(sorted_x, sorted_y)
		return (sorted_z, x + y + z)

def CountSplitInvertion(array0, array1):
	i = 0
	j = 0
	inversions = 0
	output_array = []
	while i < len(array0) and j < len(array1):
		if array0[i] <= array1[j]:
			output_array.append(array0[i])
			i += 1
		else:
			output_array.append(array1[j])
			j += 1
			inversions += len(array0) - i

	while i < len(array0):
		output_array.append(array0[i])
		i += 1
	while j < len(array1):
		output_array.append(array1[j])
		j += 1
	return (output_array, inversions)

sorted_array, num_inversions = CountInvertion(numbers)
print("Number of inversions is "+str(num_inversions))
