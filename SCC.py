'''
The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph. 

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100". If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0".

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.

@author: Ra - Denis Kotov
answer: [434821, 968, 459, 313, 211]
'''

import resource, sys
import time
from copy import copy
import collections
from directed_graph import DirectedGraph as DirectedGraph

class KosarajuSCC(object):
	t = 0
	s = None

	def __init__(self, graph):
		self.graph = graph
		self.graph_rev = self.__reverse(self.graph)
		self.graph.visited = {}
		self.graph_rev.visited = {}
		self.graph.finish_time = {}
		self.graph.time_nodes = {}
		self.graph.leader = {}
	
	def __reverse(self, graph):
		graph_rev = DirectedGraph()
		for node, edges in graph.nodes.items():
			graph_rev.addEdge(node, None)
			for edge_node in edges:
				graph_rev.addEdge(edge_node, node)
		return graph_rev
	
	def Calculate(self):
		self.__DFSLoop_rev(self.graph_rev)
		return self.__DFSLoop(self.graph)
	
	def __DFSLoop_rev(self, graph):
		i = len(graph.nodes)
		while i > 0:
			if str(i) not in graph.visited:
				self.__DFS_rev(graph, str(i))
			i -= 1
	
	def __DFS_rev(self, graph, i):
		graph.visited[i] = True
		for edge_node in graph.nodes[i]:
			if edge_node not in graph.visited:
				self.__DFS_rev(graph, edge_node)
		self.t += 1
		self.graph.finish_time[i] = str(self.t)
		self.graph.time_nodes[self.graph.finish_time[i]] = str(i)

	def __DFSLoop(self, graph):
		t = self.t
		num_scc = 0
		scc_sizes = []
		while t > 0:
			if str(t) not in graph.visited:
				self.s = t
				scc_sizes.append(self.__DFS(graph, str(t)))
				num_scc += 1
			t -= 1
		scc_sizes = sorted(scc_sizes, reverse=True)
		return scc_sizes[0:5]

	def __DFS(self, graph, t):
		component_size = 1
		graph.visited[t] = True
		self.graph.leader[t] = self.s
		for edge_node in graph.nodes[self.graph.time_nodes[t]]:
			if self.graph.finish_time[edge_node] not in graph.visited:
				component_size += self.__DFS(graph, self.graph.finish_time[edge_node])
		return component_size

if __name__ == '__main__':
	resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
	sys.setrecursionlimit(10**6)
	file = open("SCC.txt", 'r')
	graph = DirectedGraph()
	for line in file:
		array = line.split(' ')
		graph.addEdge(array[0], None)
		for num in array[1:]:
			if num != '\n' and num != '':
				graph.addEdge(num, None)
				graph.addEdge(array[0], num)
	scc = KosarajuSCC(graph)
	print(str(scc.Calculate()))
