import heapq

class MaxHeapObj(object):
	def __init__(self,val): self.val = val
	def __lt__(self,other): return self.val > other.val
	def __eq__(self,other): return self.val == other.val
	def __str__(self): return str(self.val)

class MinHeap(object):
	def __init__(self): self.h = []
	def heappush(self,x): heapq.heappush(self.h,x)
	def heappop(self): return heapq.heappop(self.h)
	def pop(self): return self.h[0]
	def __getitem__(self,i): return self.h[i]
	def __len__(self): return len(self.h)
  
class MaxHeap(MinHeap):
	def heappush(self,x): heapq.heappush(self.h,MaxHeapObj(x))
	def heappop(self): return heapq.heappop(self.h).val
	def pop(self): return self.h[0].val
	def __getitem__(self,i): return self.h[i].val

if __name__ == '__main__':
	file = open("Median.txt", 'r')
	
	medians_sum = 0
	minSub = MaxHeap()
	maxSub = MinHeap()
	
	file = open("Median.txt", 'r')
	for line in file:
		num = int(line)
		print (num)
		if len(maxSub) == 0 and len(minSub) == 0:
			maxSub.heappush(num)
		elif len(maxSub) == 0:
			if minSub.pop() >= num:
				minSub.heappush(num)
			else:
				maxSub.heappush(num)
		elif len(minSub) == 0:
			if maxSub.pop() <= num:
				maxSub.heappush(num)
			else:
				minSub.heappush(num)
		else:
			if minSub.pop() >= num:
				minSub.heappush(num)
			elif maxSub.pop() <= num:
				maxSub.heappush(num)
			else:
				minSub.heappush(num)
		
		# Balance heap
		if abs(len(maxSub) - len(minSub)) == 2:
			if len(maxSub) > len(minSub):
				minSub.heappush(maxSub.heappop())
			else:
				maxSub.heappush(minSub.heappop())
		
		size = len(minSub) + len(maxSub)
		if size % 2 == 0:
			index = size // 2
		else:
			index = (size + 1) // 2
		if index == len(minSub):
			median = minSub.pop()
		else:
			median = maxSub.pop()
		print ("median is ", median)
		print ("size is ", size)
		if minSub:
			print ("minSub.pop() is ", minSub.pop(), " size is ", len(minSub))
		if maxSub:
			print ("maxSub.pop() is ", maxSub.pop(), " size is ", len(maxSub))
		medians_sum += median
	
	print("Result is ", medians_sum % 10000)
