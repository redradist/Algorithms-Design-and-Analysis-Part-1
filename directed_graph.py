import sys
import time
from copy import copy
import collections

class DirectedGraph(object):
	def __init__(self):
		self.nodes = {}
	
	def addEdge(self, node_num, node_edge):
		if node_num not in self.nodes:
			self.nodes[node_num] = []
		if node_edge is not None:
			self.nodes[node_num].append(node_edge)
		
	def __str__(self):
		return self.nodes