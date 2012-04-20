from __future__ import print_function

def logw(str_):
	print(str_)
	
def log(*args):
	print(" ".join([str(a) for a in args]))
	pass


set_ = set()
	
filename = "HashInt.txt"
ts_filename = "TargetSums.txt"

str_ = open(filename, 'r').read()
list_ = [int(elem) for elem in str_.split()]

str_ = open(ts_filename, 'r').read()
ts_list = [int(elem) for elem in str_.split(',')]

for el in list_:
	set_.add(el)

print(ts_list)	

for sum_ in ts_list:
	result = 0
	for i in list_:
		second = sum_ - i
		if second in set_:
			result = 1 
			break
		
	print(result, end="")
# print list_
# print ts_list