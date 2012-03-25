def log(val):
	#print val
	pass

def count_inv(list):
	list_len = len(list)
	log("list length {0}".format(list_len))
	half = list_len/2
	
	if half==0:
		return (list,0)
	
	left_list = list[:half]
	right_list = list[half:]
	
	log("left list {0}".format(left_list))
	log("right list {0}".format(right_list))
	
	left_result = count_inv(left_list)
	right_result = count_inv(right_list)
	
	sorted_left_list = left_result[0]
	sorted_right_list = right_result[0]
	
	left_inv_count = left_result[1]
	right_inv_count = right_result[1]

	sorted_list = []
	left_i = 0
	right_i = 0
	split_inv_count = 0
	
	for i in range(0,list_len):
		log("i = {0}".format(i))
		log("left i = {0}".format(left_i))
		log("right i = {0}".format(right_i))
		if left_i < len(sorted_left_list) \
				and (right_i >= len(sorted_right_list) \
					or int(sorted_left_list[left_i])<int(sorted_right_list[right_i])):
			log("copy left")
			sorted_list.append(sorted_left_list[left_i])
			left_i+=1
		else:
			log("copy right")
			sorted_list.append(sorted_right_list[right_i])
			right_i+=1
			split_inv_count += (len(sorted_left_list)-left_i)
		log("split inv count = {0}".format(split_inv_count))
	
	inv_count = left_inv_count + right_inv_count + split_inv_count
	
	log("inv count {0}".format(inv_count))
	return (sorted_list,inv_count)

#for test
#str = "1 10 4 3 2 11"
#str = "1 3 5 2 4 6"
#lst = str.split()

filestring = open('IntegerArray.txt', 'r').read()
lst = filestring.split()

result = count_inv(lst)
print "sorted list: {0}".format(result[0])
print "inversion count: {0}".format(result[1])