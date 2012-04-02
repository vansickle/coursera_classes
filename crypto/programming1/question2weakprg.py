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
		print self.x
		self.y = random.randint(0, p)
		print self.y

	def next(self):
		# x_{i+1} = 2*x_{i}+5  (mod p)
		self.x = (2*self.x + 5) % self.p

		# y_{i+1} = 3*y_{i}+7 (mod p)
		self.y = (3*self.y + 7) % self.p

		# z_{i+1} = x_{i+1} xor y_{i+1}
		return (self.x ^ self.y) 


prng = WeakPrng(P)

list = []
for i in range(1, 10):
	val = prng.next()
	list.append(val)
	print "output #%d: %d" % (i, val)

print list

#output = [210205973, 22795300, 58776750, 121262470, 264731963, 140842553, 242590528, 195244728, 86752752]

x = 92134638
y = 2664024
output = [176311022L, 84750146L, 210265938L, 492796695L, 
303683767L, 460399902L, 471367820L, 340585377L, 52435122L]

prng = WeakPrng(P)
prng.x = x
prng.y = y
print prng.next()

test_p = 10000
prng = WeakPrng(test_p)
lst_ = [prng.next() for i in range(1,10)]
print lst_
known_ = lst_[:-1]
print known_

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

from time import time
	
start = time()
result = break_prng(known_, test_p)
elapsed = (time() - start)
print "result x = {0} y = {1} next = {2}".format(result.x, result.y, result.next)
print "elapsed : {0}".format(elapsed)

#assert result.x == 10
#assert result.y == 1
assert result.next == lst_[-1]
