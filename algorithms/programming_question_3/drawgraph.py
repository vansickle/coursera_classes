"""
Draw graph
@author: Pavel Samokha
@url: 
"""
import pydot
import os
import sys

def view_in_default_app(filename):
	platform = sys.platform
	if platform == "win32":
		os.startfile(filename)
	elif platform == "darwin": #osx
		os.popen('open '+filename)

def add_nodes(graph, list_):
	nodes_dict = dict()
	
	for adjlist in list_:
		vertex = adjlist[0]
		node = pydot.Node(str(vertex))
		graph.add_node(node)
		nodes_dict[vertex] = node
	
	
	for adjlist in list_:
		vertex = adjlist[0]
		node = nodes_dict[vertex]
		for adjvertex in adjlist[1:]:
			
			if adjvertex < vertex: #remove duplicate nodes
				continue
			
			adj_node = nodes_dict[adjvertex]
			graph.add_edge(pydot.Edge(node, adj_node))
			
def draw_and_view(list_):
	
	graph = pydot.Dot(graph_type='graph')

	add_nodes(graph, list_)

	graph.write_png('graph.png')

	view_in_default_app('graph.png')
	
#for test
str_ = """1 2 3
2 1 3 4
3 1 2 4
4 2 3"""
list_ = str_.split()

str_ = open('kargerAdj.txt', 'r').read()
list_ = str_.split('\n')

list_ = [ line.split() for line in list_ ]

draw_and_view(list_)