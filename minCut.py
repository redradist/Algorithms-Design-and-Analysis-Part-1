import random
import copy

class Edge(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b
		
	def __eq__(self, edge):
		return (self.a == edge.a and self.b == edge.b) or (self.b == edge.a and self.a == edge.b)
		
	def __ne__(self, edge):
		print("__ne__")
		return not self.__eq__(edge)
		
	def __copy__(self):
		newone = type(self)(self.a, self.b)
		return newone
	
	def __str__(self):
		return "self.a is "+str(self.a)+", self.b is "+str(self.b)
		
class UndirectedGraph(object):
	def __init__(self):
		self.nodes = {}
	
	def addEdge(self, node_num, node_edge):
		if node_num not in self.nodes:
			self.nodes[node_num] = []
		if node_edge is not None:
			self.nodes[node_num].append(node_edge)
	
	def hasEdge(self, node_num, node_edge):
		if node_num not in self.nodes:
			return False
		elif node_edge in self.nodes[node_num]:
			return True
	
	def __copy__(self):
		newone = type(self)()
		newone.nodes = copy.deepcopy(self.nodes)
		return newone
	
	def __str__(self):
		return self.nodes

def findMinCut(graph, edges):
	while len(graph.nodes) != 2:
		#num = random.randrange(0, len(edges), 1)
		selected_edge = copy.copy(random.choice(edges))
		if random.randrange(0, 2) == 0:
			save = selected_edge.a
			delete = selected_edge.b
		else:
			save = selected_edge.b
			delete = selected_edge.a
		
		adds = []
		removes = []
		for edge in graph.nodes[delete]:
			if edge not in graph.nodes[save]:
				adds.append(edge)
			else:
				removes.append(edge)
		del graph.nodes[delete]

		for edge in adds:
			graph.nodes[save].append(edge)
		for edge in removes:
			graph.nodes[save].remove(edge)
		
		for edge in edges:
			if edge.a == delete:
				edge.a = save
			elif edge.b == delete:
				edge.b = save
			if edge.a == edge.b:
				removes.append(edge)
		
		for edge in removes:
			edges.remove(edge)
		
	return len(edges)

if __name__ == '__main__':
	file = open("kargerMinCut.txt", 'r')
	graph = UndirectedGraph()
	edges = []
	for line in file:
		array = line.split('\t')
		graph.addEdge(array[0], None)
		for num in array[1:]:
			if num != '\n' and num != '':
				if array[0] != num:
					edge = Edge(array[0], num)
					if edge not in edges:
						graph.addEdge(array[0], edge)
						edges.append(edge)
	i = 100
	min_cut = -1
	while i > 0:
		temp_graph = copy.deepcopy(graph)
		temp_edges = copy.deepcopy(edges)
		if id(temp_graph) == id(graph):
			raise Exception("**Failure to rebuild, new dictionary is not different from the old")
		if id(temp_edges) == id(edges):
			raise Exception("**Failure to rebuild, new list is not different from the list")
		temp = findMinCut(temp_graph, temp_edges)
		print("Current min_cut is "+str(temp))
		if min_cut == -1 or temp < min_cut:
			min_cut = temp
		i -= 1
	print("Min cut is "+str(min_cut))
