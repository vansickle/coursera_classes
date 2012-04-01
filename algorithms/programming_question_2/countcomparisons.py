def sort_and_count(list_, start_item, last_item, choose_pivot):
	print "start_item: {0}".format(start_item)
	print "last_item: {0}".format(last_item)
	
	if start_item+1 >= last_item:
		return 0
	
	i = start_item
	# j = 1
	#pivot_pos = i
	print list_
	#pivot = list_[pivot_pos]
	pivot = choose_pivot(list_, start_item, last_item)
	print "pivot = {0}".format(pivot)
	
	for j in range(start_item+1, last_item):
		print "before: i = {0}; j = {1};".format(i, j)
		next = list_[j]
		print "next = {0}".format(next)
		if next < pivot.value:
			first_bigger = list_[i+1]
			list_[j] = first_bigger
			list_[i+1] = next
			i += 1
		
		print "after: i = {0}; j = {1};".format(i, j)
		print list_
	
	list_[pivot.pos] = list_[i]
	list_[i]=pivot.value
	
	print "after move pivot: {0}".format(list_)
	
	left_count = sort_and_count(list_, start_item, i, choose_pivot)
	right_count = sort_and_count(list_, i+1, last_item, choose_pivot)
	comparisons_count = last_item - start_item - 1 + left_count + right_count
	return comparisons_count

#for test
str_ = "3 10 4 1 2 11"
#str_ = "1 3 5 2 4 6"
#str_ = "3 1 4 2 6 7"
list_ = str_.split()

#filestring = open('QuickSort.txt', 'r').read()
#list_ = filestring.split()

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
	

def choose_last(list_, start_item, last_item):
	return Pivot(start_item, list_[start_item])

count = sort_and_count(list_, 0, len(list_), choose_last)
print "comparisons number for first item as pivot: {0}".format(count)
# print "comparisons number for last item as pivot: {0}".format(count)
# print "comparisons number for median item as pivot: {0}".format(count)