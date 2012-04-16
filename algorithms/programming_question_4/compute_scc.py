def logw(str_):
	print str_
	
def log(*args):
	print " ".join([str(a) for a in args])
	pass

vert_number = 0
#can change to list
vertices = dict()

vertices_dict_by_finish_times = dict()
finish_time = 0

def drill_down(vertex):
	log("starts with:", vertex)
	
	vertex.mark_as_explored()
	
	all_explored = True
	
	for edge in vertex.edges:
		log("edge:", edge)
		
		next_vertex = vertices[edge.head]
		log("next vertex", next_vertex)
		if next_vertex.is_explored():
			log("next vertex ", next_vertex, " is explored")
			continue
		
		all_explored = False
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
		vertex = vertices[i]
		log()
		log("top level vertex", vertex)
		if not vertex.is_explored():
			drill_down(vertex)
	
	# log("\nreverse list")	
	# list_ = map(lambda edge: edge.reverse(), list_)
	# log(list_)
	
	for i in xrange(vert_number, 0, -1):
		vertex = vertices[i]
		vertex.reverse()
	
		

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


str_ = open('TestData/scc_graph_1.txt', 'r').read()
vert_number = 7
# str_ = open('SCC.txt', 'r').read()
# vert_number = 875714
list_ = str_.split('\n')

list_ = [Edge(int(node_list[0]),int(node_list[1])) for node_list in [line.split() for line in list_]]

compute_scc(list_)

log(vertices)
# log(list_)