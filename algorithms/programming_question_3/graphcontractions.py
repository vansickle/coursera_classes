def logw(str_):
	print str_
	
def log(*args):
	print " ".join([str(a) for a in args])
	pass

def contract(list_):
	for adjlist in list_:
		log("vertex: ", adjlist[0])
		for adjvi in adjlist[1:]:
			log("adjacent vertex:", adjvi)
	

#for test
str_ = """1 2 3
2 1 3 4
3 1 2 4
4 2 3"""
#list_ = str_.split()

# str_ = open('kargerAdj.txt', 'r').read()
#filestring = open('samples/array3.txt', 'r').read()
list_ = str_.split('\n')

list_ = [ line.split() for line in list_ ]

contract(list_)

log(list_)