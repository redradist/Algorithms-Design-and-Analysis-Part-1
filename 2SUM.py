from bisect import *

def find_lt(a, x):
    'Find rightmost value less than x'
    index = bisect_left(a, x)
    if index:
        return index-1
    return None

def find_gt(a, x):
    'Find leftmost value greater than x'
    index = bisect_right(a, x)
    if index != len(a):
        return index
    return None

if __name__ == '__main__':
	list_ = {}
	for ran_num in range(-10000, 10001):
		list_[ran_num] = False

	intergers = []
	
	num_target = 0
	file = open("algo1-programming_prob-2sum.txt", 'r')
	lines = file.readlines()
	for line in lines:
		num = int(line)
		intergers.append(num)
	print("Finished filling hashtable")
	print("Sorting ...")
	intergers.sort()
	print("Array sorted")
	progress = 0
	size = len(intergers)
	for interger in intergers:
		print("Progress is ",progress/float(size))
		y_high = 10000 - interger
		y_low = -10000 - interger
		if y_high < y_low:
			temp = y_high
			y_high = y_low
			y_low = temp
		
		lower_bound = find_lt(intergers, y_low)
		upper_bound = find_gt(intergers, y_high)
		#print("y_low is ", y_low, " lower_bound is ", lower_bound)
		#print("y_high is ", y_high, " upper_bound is ", upper_bound)
		#print("lower_bound value is ", intergers[lower_bound] if lower_bound else "")
		#print("upper_bound value is ", intergers[upper_bound] if upper_bound else "")
		start = 0
		end = 0
		if lower_bound != None or upper_bound != None:
			if lower_bound != None and upper_bound != None:
				delta = upper_bound - lower_bound - 1
				start = lower_bound + 1
				end = upper_bound
			elif lower_bound != None:
				delta = size - lower_bound - 1
				start = lower_bound + 1
				end = 1000000
			else:
				delta = upper_bound
				start = 0
				end = upper_bound
		num_target += delta
		for ran_num in range(start, end):
			if progress != ran_num:
				list_[interger+intergers[ran_num]] = True
		progress += 1
	num_target = 0
	for key, value in list_.items():
		if value == True:
			num_target += 1
	print("Result is ", num_target)
