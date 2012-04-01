def sort_and_count(list_, start_item, last_item):
	print "start_item: {0}".format(start_item)
	print "last_item: {0}".format(last_item)
	
	if start_item+1 >= last_item:
		return 0
	
	i = start_item
	# j = 1
	pivot_pos = i
	print list_
	pivot = list_[pivot_pos]
	print "pivot = {0}".format(pivot)
	
	for j in range(start_item+1, last_item):
		print "before: i = {0}; j = {1};".format(i, j)
		next = list_[j]
		print "next = {0}".format(next)
		if next < pivot:
			first_bigger = list_[i+1]
			list_[j] = first_bigger
			list_[i+1] = next
			i += 1
		
		print "after: i = {0}; j = {1};".format(i, j)
		print list_
	
	list_[pivot_pos] = list_[i]
	list_[i]=pivot
	
	print "after move pivot: {0}".format(list_)
	
	left_count = sort_and_count(list_, start_item, i)
	right_count = sort_and_count(list_, i+1, last_item)
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
count = sort_and_count(list_, 0, len(list_))

print "comparisons number: {0}".format(count)