def logw(str_):
	print str_
	
def log(*args):
	print " ".join([str(a) for a in args])
	pass

vertices = dict()
	
#need to have ordered list of vertices
#cause dict.items() not ordered
vertices_list = list()

vertices_dict_by_finish_times = dict()
vertices_list_by_finish_times = list()

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
	vertices_list_by_finish_times.insert(0, vertex)
	vertices_dict_by_finish_times[vertex.finish_time] = vertex
	log("vertex ", vertex, "finish time:", finish_time)

def compute_scc(list_):
	
	logw("starts computing")
	list_ = reversed(list_)
	logw("reversed")
	for edge in list_:
		if edge.tail not in vertices:
			vertex = Vertex(edge.tail)
			vertices[edge.tail] = vertex
			vertices_list.append(vertex)
		
		vertex = vertices[edge.tail]
		vertex.add_edge(edge)
		
		# log("edge: ", edge)
		#for adjvi in adjlist[1:]:
		#	log("adjacent vertex:", adjvi)
	logw("done building vertices dictionary")
	log("vertices:", vertices)
	log("vertices list:", vertices)
	
	for vertex in vertices_list:
		log()
		log("top level vertex", vertex)
		if not vertex.is_explored():
			drill_down(vertex)
		
	log(list_)
	map(lambda edge: edge.rotate(), )
		

class Vertex(object):
	def __init__(self, number):
		super(Vertex, self).__init__()
		self.number = number
		self.edges = []
		self.explored = False
		self.finish_time = 0
		
	def add_edge(self, edge):
		self.edges.append(edge)
		
	def mark_as_explored(self):
		self.explored = True
	
	def is_explored(self):
		return self.explored
		
	def is_finished(self):
		return self.finish_time>0
		
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
		return self.__str__()
	
	def rotate

str_ = open('TestData/scc_graph_1.txt', 'r').read()
# str_ = open('SCC.txt', 'r').read()
list_ = str_.split('\n')

list_ = [Edge(node_list[0],node_list[1]) for node_list in [line.split() for line in list_]]

compute_scc(list_)

log(vertices_list_by_finish_times)
# log(list_)