def logw(str_):
	print str_
	
def log(*args):
	print " ".join([str(a) for a in args])
	pass

def compute_scc(list_):
	for edge in list_:
		log("edge: ", edge)
		#for adjvi in adjlist[1:]:
		#	log("adjacent vertex:", adjvi)

class Edge(object):
	def __init__(self, tail, head):
		super(Edge, self).__init__()
		self.tail = tail
		self.head = head
		
	def __str__(self):
		return "{0} => {1}".format(self.tail, self.head)

	def __repr__(self):
		return self.__str__();


str_ = open('TestData/scc_graph_1.txt', 'r').read()
#filestring = open('samples/array3.txt', 'r').read()
list_ = str_.split('\n')

list_ = [Edge(node_list[0],node_list[1]) for node_list in [line.split() for line in list_]]

compute_scc(list_)

log(list_)