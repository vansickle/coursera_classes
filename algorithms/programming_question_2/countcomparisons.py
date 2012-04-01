'''it works but definitely code requires refactoring'''
def logw(str_):
	print str_
	
def log(str_):
	# print str_
	pass

def sort_and_count(list_, start_item, last_item, choose_pivot):
	log("start_item: {0}".format(start_item))
	log("last_item: {0}".format(last_item))
	
	if start_item+1 >= last_item:
		return 0
	
	i = start_item
	# j = 1
	#pivot_pos = i
	log(list_)
	#pivot = list_[pivot_pos]
	pivot = choose_pivot(list_, start_item, last_item)
	log("pivot = {0}".format(pivot))
	
	list_[pivot.pos] = list_[start_item]
	list_[start_item] = pivot.value
	log("after pivot move to first place: {0}".format(list_))
	
	for j in range(start_item+1, last_item):
		log("before: i = {0}; j = {1};".format(i, j))
		next = list_[j]
		log("next = {0}".format(next))
		if next < pivot.value:
			first_bigger = list_[i+1]
			list_[j] = first_bigger
			list_[i+1] = next
			i += 1
		
		log("after: i = {0}; j = {1};".format(i, j))
		log(list_)
	
	list_[start_item] = list_[i]
	list_[i]=pivot.value
	
	log("after move pivot: {0}".format(list_))
	
	left_count = sort_and_count(list_, start_item, i, choose_pivot)
	right_count = sort_and_count(list_, i+1, last_item, choose_pivot)
	comparisons_count = last_item - start_item - 1 + left_count + right_count
	return comparisons_count

#for test
str_ = "3 10 4 1 2 11"
#str_ = "11 10 4 1 2 3"
#str_ = "1 3 5 2 4 6"
#str_ = "3 1 4 2 6 7"
str_ = "10 5 7 3 6 9 12 67 32 45 54 2 1"
#list_ = str_.split()

filestring = open('QuickSort.txt', 'r').read()
#filestring = open('samples/array3.txt', 'r').read()
list_ = filestring.split()
list_ = [ int(x) for x in list_ ]

class Pivot(object):
	def __init__(self, pos, value):
	 	super(Pivot, self).__init__()
	 	self.pos = pos
	 	self.value = value
	
	def __str__(self):
		return "Pivot [pos = {0}, value = {1}]".format(self.pos, self.value)
	
	def __repr__(self):
		return "Pivot [pos = {0}, value = {1}]".format(self.pos, self.value)
	

def choose_first(list_, start_item, last_item):
	return Pivot(start_item, list_[start_item])
	
def choose_last(list_, start_item, last_item):
	return Pivot(last_item-1, list_[last_item-1])

def choose_median(list_, start_item, last_item):
	start_value = list_[start_item]
	last_value = list_[last_item-1]
	
	#for two elems
	if (last_item - start_item) == 2:
		return Pivot(start_item, start_value)
	
	middle_pos = start_item+int(round(float(last_item - start_item)/2))-1
	middle_value = list_[middle_pos]
	log("middle pos: {0}".format(middle_pos))
	
	#not good - but can be implemented with ifels
	elems = {last_item-1: last_value, middle_pos: middle_value, start_item: start_value}
	sorted_ = sorted(elems, key=elems.get)
	log("sorted: {0}".format(sorted_))
	log("sorted: {0}".format(["{0}:{1}".format(x,elems.get(x)) for x in sorted_ ]))
	median_pos = sorted_[1]

	return Pivot(median_pos, list_[median_pos])

print "=========== first ============="
count_for_first = sort_and_count(list_, 0, len(list_), choose_first)
print list_

list_ = filestring.split()
list_ = [ int(x) for x in list_ ]

print "=========== last ============="
count_for_last = sort_and_count(list_, 0, len(list_), choose_last)
print list_
# 
# 
list_ = filestring.split()
# list_ = str_.split()
list_ = [ int(x) for x in list_ ]

print "=========== median ============="
count_for_median = sort_and_count(list_, 0, len(list_), choose_median)
print list_


print "comparisons number for first item as pivot: {0}".format(count_for_first)
print "comparisons number for last item as pivot: {0}".format(count_for_last)
print "comparisons number for median item as pivot: {0}".format(count_for_median)