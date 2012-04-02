import random

def logw(str_):
	print str_
	
def log(str_):
	# print str_
	pass

P = 295075153L	 # about 2^28

class WeakPrng(object):
	def __init__(self, p):	 # generate seed with 56 bits of entropy
		self.p = p
		self.x = random.randint(0, p)
		self.y = random.randint(0, p)
		
	def next(self):
		# x_{i+1} = 2*x_{i}+5  (mod p)
		self.x = (2*self.x + 5) % self.p
		self.mod_x = (2*self.x + 5) / self.p
		# y_{i+1} = 3*y_{i}+7 (mod p)
		self.y = (3*self.y + 7) % self.p
		self.mod_y = (3*self.y + 7) / self.p

		# z_{i+1} = x_{i+1} xor y_{i+1}
		return (self.x ^ self.y) 

# prng = WeakPrng(P)
# 
# list = []
# for i in range(1, 10):
# 	val = prng.next()
# 	list.append(val)
# 	print "output #%d: %d" % (i, val)
# 
# print list

output = [210205973L, 22795300L, 58776750L, 121262470L, 264731963L, 140842553L, 242590528L, 
195244728L, 86752752L]

#x = 92134638
#y = 2664024
#output = [176311022L, 84750146L, 210265938L, 492796695L, 
#303683767L, 460399902L, 471367820L, 340585377L, 52435122L]

# prng = WeakPrng(P)
# prng.x = x
# prng.y = y
# print prng.next()

test_p = 100000
prng = WeakPrng(test_p)
start_x = prng.x
start_y = prng.y

lst_ = []
info = []
for i in range(1,10):
	val = prng.next()
	lst_.append(val)
	info.append("x={0} mod_x={1} y={2} mod_y={3} val={4}".format(prng.x, prng.mod_x, prng.y, prng.mod_y, val))

# lst_ = [prng.next() for i in range(1,10)]
print "test data start_x={0} start_y={1} seq={2}".format(start_x,start_y,lst_)
print "full test data {0}".format(info)
known_ = lst_[:-1]
print "sequence for break (known part): {0}".format(known_)

#x = 10
#y = 1
#known_ = [5, 2, 13, 4, 5, 2, 13, 4] #uknown 5

class Result(object):
	"""docstring for Result"""
	def __init__(self,x,y,next):
		super(Result, self).__init__()
		self.x = x
		self.y = y
		self.next = next
	
	def __str__(self):
		return "Result [x = {0}, y = {1}, next = {2}]".format(self.x, self.y, self.next)
	
	def __repr__(self):
		return __str__(self)

def break_prng(known_, p):
	prng = WeakPrng(p)
	
	for x in range(0,p):
		if x%100 == 0:
			logw("breaking step x={0}".format(x))
		
		for y in range(0, p):
			check = True
			prng.x = x
			prng.y = y
			log("x = {0}".format(prng.x))
			log("y = {0}".format(prng.y))
			for i in range(0, len(known_)):
				prng_next = prng.next()
				log("prng_next = {0}".format(prng_next))
				if prng_next!=known_[i]:
					check=False
					break
			if check == True:
				res = Result(x, y, prng.next())
				return res
	return Result(0,0,0)


global_count = 0

from threading import Thread
import threading

def multithreaded_break_prng_backwards(known_, p):
	count = 4
	for i in range(count):
	    t = Thread(target=break_prng_backwards_internal, args=(known_, p, p/count*i, p/count*(i+1)))
	    t.start()
	    logw("thread {0} started".format(i))

	for thread in threading.enumerate():
		if thread is not threading.currentThread():
			thread.join()


from multiprocessing import Process

def multiprocessing_break_prng_backwards(known_, p):
	count = 4

	proc_list = []

	for i in range(count):
		start = p/count*i
		end = p/count*(i+1)
		p = Process(target=break_prng_backwards_internal, args=(known_, p, start, end))
		proc_list.append(p)
		p.start()
		logw("Process {0} started".format(i))

	for proc in proc_list:
		proc.join()

def break_prng_backwards(known_, p):
	return break_prng_backwards_internal(known_, p, 0, p)

def break_prng_backwards_internal(known_, p, start_p, end_p):
	logw("start_p = {0}, end_p = {1}".format(start_p,end_p))

	global global_count
	for last_x in xrange(start_p, end_p):

		if (last_x + 1 - start_p) % 10000 == 0:
		 	global_count += 10000
		 	logw("global count = {0}".format(global_count))

		x = last_x
		check = True
		log("x = {0}".format(x))
		for i in range(0, len(known_)-1):
			log ("i = {0}".format(i))
			check = False
			
			for x_mod in range (0,3):
				log("x_mod = {0}".format(x_mod))
				check = True
				x_prev = (x + x_mod * p - 5)/2
			
				log("x_prev:{0}".format(x_prev))
				
				if x_prev < 0:
					continue
		
				known_xy = known_[-(i+1)]
			
				log("known x^y = {0}".format(known_xy))
				y = known_xy ^ x
				
				check = False
				for y_mod in range (0, 4):
					y_prev = (y + y_mod * p - 7)/3
				
					log("y_mod = {0}".format(y_mod))
					log("y_prev = {0}".format(y_prev))
			
					if y_prev < 0:
						continue
			
					prng_prev = x_prev ^ y_prev
			
					log("prng_prev:{0}".format(prng_prev))
			
					known_xy_prev = known_[-(i+2)]
					log("known_xy_prev = {0}".format(known_xy_prev))
			
					if  known_xy_prev==prng_prev:
						check = True
						log("y_mod ok!")
						break
				
				if check == True:
					log("x_mod ok!")
					y = y_prev
					x = x_prev
					break
					
			if check == False:
				break
				
		if check == True:
			prng = WeakPrng(p)
			prng.x = last_x
			prng.y = known_[-1]^last_x
			result = Result(prng.x, prng.y, prng.next())
			logw("found solution! = {0}".format(result))
			return result
			# import sys
			# sys.exit("Found")
	return Result(0,0,0)
	
from time import time

print "======== backward break ========="
start = time()
result = break_prng_backwards(known_, test_p)
# result = multithreaded_break_prng_backwards(known_, test_p)
# result = multiprocessing_break_prng_backwards(known_, test_p)
# result = multithreaded_break_prng_backwards(output, P)
elapsed = (time() - start)
print "elapsed : {0}".format(elapsed)
print "result x = {0} y = {1} next = {2}".format(result.x, result.y, result.next)

#assert result.x == 10
#assert result.y == 1
assert result.next == lst_[-1]

# 
# print "========= brute force break =========="
# start = time()
# result = break_prng(known_, test_p)
# elapsed = (time() - start)
# print "result x = {0} y = {1} next = {2}".format(result.x, result.y, result.next)
# print "elapsed : {0}".format(elapsed)
# 
# #assert result.x == 10
# #assert result.y == 1
# assert result.next == lst_[-1]
