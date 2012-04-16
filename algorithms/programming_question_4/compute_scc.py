#NB! Algorithm works, but very ineffective in terms of memory (and speed too) - have no time to improve

import sys, thread, threading, time

enable_log = False

def logw(*args):
	print " ".join([str(a) for a in args])
	
def log(*args):
	if enable_log:
		print " ".join([str(a) for a in args])

vert_number = 0
#can change to list
vertices = dict()

vertices_dict_by_finish_times = dict()
finish_time = 0

leader = None
scc_vertices_number = 0
scc = []

max_scc = []
max_scc_count = 5

def stage2(vertex):
	global scc_vertices_number
	scc_vertices_number += 1
	scc.append(vertex)
	vertex.mark_as_explored()

	for edge in vertex.edges:
		next_vertex = vertices[edge.head]
		log("next vertex", next_vertex)
		if next_vertex.is_explored():
			log("next vertex ", next_vertex, " is explored")
			continue
		
		stage2(next_vertex)
		


def drill_down(vertex):
	log("starts with:", vertex)
	
	vertex.mark_as_explored()
	
	for edge in vertex.edges:
		log("edge:", edge)
		
		next_vertex = vertices[edge.head]
		log("next vertex", next_vertex)
		if next_vertex.is_explored():
			log("next vertex ", next_vertex, " is explored")
			continue
		
		drill_down(next_vertex)
		
	# if all_explored:
	global finish_time
	finish_time += 1
	vertex.finish_time = finish_time
	vertices_dict_by_finish_times[vertex.finish_time] = vertex
	log("vertex ", vertex, "finish time:", finish_time)

def compute_scc(list_):
	
	logw("starts computing")
	reversed_list = reversed(list_)
	logw("reversed")
	for edge in reversed_list:
		if edge.tail not in vertices:
			vertex = Vertex(edge.tail)
			vertices[edge.tail] = vertex
		
		vertex = vertices[edge.tail]
		vertex.add_edge(edge)
		
		if edge.head not in vertices:
			head_vertex = Vertex(edge.head)
			vertices[edge.head] = head_vertex
		
		head_vertex = vertices[edge.head]
		head_vertex.add_inc_edge(edge)
		
		# log("edge: ", edge)
		#for adjvi in adjlist[1:]:
		#	log("adjacent vertex:", adjvi)
	logw("done building vertices dictionary")
	log("vertices:", vertices)
	log("vertices list:", vertices)
	
	for i in xrange(vert_number,0,-1):
		if i%10000==0:
			logw("stage 1 on:", i)
		vertex = vertices[i]
		log("\ntop level vertex", vertex)
		if not vertex.is_explored():
			drill_down(vertex)

	# log("\nreverse list")	
	# list_ = map(lambda edge: edge.reverse(), list_)
	# log(list_)
	
	for i in xrange(vert_number, 0, -1):
		vertex = vertices[i]
		vertex.reverse()
			
	logw("stage 2")
	for i in xrange(vert_number, 0, -1):
		vertex = vertices_dict_by_finish_times[i]
		log("\nvertex", vertex)
		
		if i%10000 == 0:
			logw("stage 2 on:", i)

		if not vertex.is_explored():
			global scc
			scc = []
			global scc_vertices_number
			scc_vertices_number = 0
			leader = vertex
			stage2(vertex)
			log("Found SCC:", scc, "Vertices number:", scc_vertices_number)
			
			global max_scc
			global max_scc_count

			max_scc.append(scc_vertices_number)
			max_scc = sorted(max_scc)

			log("max scc:", max_scc)
			max_scc = max_scc[-max_scc_count:]

			# if len(max_scc)<max_scc_count:
			# 	max_scc.append(scc_vertices_number)
			# 	max_scc = sorted[max_scc]
			# else
			# 	max_scc.append
				

class Vertex(object):
	def __init__(self, number):
		super(Vertex, self).__init__()
		self.number = number
		self.edges = []
		self.inc_edges = []
		self.explored = False
		self.finish_time = 0
		
	def add_edge(self, edge):
		self.edges.append(edge)
	
	def add_inc_edge(self, edge):
		self.inc_edges.append(edge)
	
	def mark_as_explored(self):
		self.explored = True
	
	def is_explored(self):
		return self.explored
		
	def is_finished(self):
		return self.finish_time>0
	
	def reverse(self):
		map(lambda edge: edge.reverse(), self.edges)
		self.explored = False
		self.edges, self.inc_edges = self.inc_edges, self.edges
		
	def __str__(self):
		return "{0} : {1}".format(self.number, self.edges)

	def __repr__(self):
		return self.__str__();

class Edge(object):
	def __init__(self, tail, head):
		super(Edge, self).__init__()
		self.tail = tail
		self.head = head
		
	def __str__(self):
		return "{0} => {1}".format(self.tail, self.head)

	def __repr__(self):
		return self.__str__();

	def reverse(self):
		self.tail, self.head = self.head, self.tail
		return self

# enable_log = True
# filename = 'TestData/scc_graph_1.txt'
# vert_number = 7
# max_scc_count = 1

# enable_log = True
# filename = 'TestData/scc_graph_2.txt'
# vert_number = 10
# max_scc_count = 2

# enable_log = True
# filename = 'TestData/scc_graph_3.txt'
# vert_number = 15
# max_scc_count = 4

# enable_log = True
# filename = 'TestData/scc_graph_4.txt'
# vert_number = 5
# max_scc_count = 4

# enable_log = True
# filename = 'TestData/scc_graph_5.txt'
# vert_number = 9
# max_scc_count = 3

logw("starts")

filename = 'SCC.txt'
vert_number = 875714
max_scc_count = 5

def all():

	count = 0
	list_ = []
	with open(filename, 'r') as f:
		for line in f:
			node_list = line.split()
			edge = Edge(int(node_list[0]),int(node_list[1]))
			list_.append(edge)
			count += 1
			if count % 50000 == 0:
				logw("edges loaded from file:", count)

	compute_scc(list_)
	logw(list(reversed(max_scc)))

# need to overcome recursion depth limits in python
# other way - rewrite recursion to loop using own stack
sys.setrecursionlimit(100000)   
thread.stack_size(2**27)      #just big size
thread = threading.Thread( target = all )

start_time = time.clock()
thread.start()      
thread.join()
print time.clock() - start_time