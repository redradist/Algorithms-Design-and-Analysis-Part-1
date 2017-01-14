from heapq import *

class DijkstraShortPath(object):
	def __init__(self, Size):
		self.Vertices = []
		self.Neighbors = {}
		self.Distance = {}
		self.ShortPathsHeap = []

	def addVertex(self, vertex):
		self.Vertices.append(vertex)

	def addEdge(self, vertex, neighbor, lenght):
		if vertex not in self.Neighbors:
			self.Neighbors[vertex] = []
		self.Neighbors[vertex].append((neighbor, lenght))

	def computeShortPath(self, source):
		self.Distance[source] = 0
		for vertex in self.Vertices:
			if vertex != source:
				self.Distance[vertex] = 1000000
			heappush(self.ShortPathsHeap, (self.Distance[vertex], vertex))
		while self.ShortPathsHeap:
			min_distance, next_vertex = heappop(self.ShortPathsHeap)
			print("min_distance ", min_distance, " next_vertex ", next_vertex)
			for vertex, lenght in self.Neighbors[next_vertex]:
				alt = min_distance + lenght
				if alt < self.Distance[vertex]:
					self.ShortPathsHeap.remove((self.Distance[vertex], vertex))
					self.Distance[vertex] = alt
					heapify(self.ShortPathsHeap)
					heappush(self.ShortPathsHeap, (self.Distance[vertex], vertex))

if __name__ == '__main__':
	file = open("dijkstraData.txt", 'r')
	shortPath = DijkstraShortPath(200)
	vetreces = []
	for line in file:
		array = line.split('\t')
		shortPath.addVertex(int(array[0]))
		for edge in array[1:]:
			if ',' in edge:
				edge_weight = edge.split(',')
				print("Vertix is ",edge_weight[0]," Weight is ", edge_weight[1])
				shortPath.addEdge(int(array[0]), int(edge_weight[0]), int(edge_weight[1]))
	shortPath.computeShortPath(1)
	print(shortPath.Distance[7])
	print(shortPath.Distance[37])
	print(shortPath.Distance[59])
	print(shortPath.Distance[82])
	print(shortPath.Distance[99])
	print(shortPath.Distance[115])
	print(shortPath.Distance[133])
	print(shortPath.Distance[165])
	print(shortPath.Distance[188])
	print(shortPath.Distance[197])
	