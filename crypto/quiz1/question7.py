import sys

def splitCount(s, count):
     return [''.join(x) for x in zip(*[list(s[z::count]) for z in range(count)])]

pt1 = 'attack at dawn'
ct1 = '6c73d5240a948c86981bc294814d'
pt2 = 'attack at dusk'
ct2 = ''

lst = splitCount(ct1,2)

for i in range(0,len(lst)):
	pt1num = int(hex(ord(pt1[i])), 16)
	print 'pt1num = '
	print 'pt1num = {0}'.format(pt1num)
	print 'pt1num_bin = {0}'.format(bin(pt1num))
	
	ct1num = int('0x'+lst[i], 16)
	print 'ct1num = {0}'.format(ct1num)
	print 'ct1num_bin = {0}'.format(bin(ct1num))

	pt2num = int(hex(ord(pt2[i])), 16)
	print 'pt2num = {0}'.format(pt2num)
	print 'pt2num_bin = {0}'.format(bin(pt2num))
	
	xor = pt1num^ct1num
	print "xor = {0}".format(xor)
	print "xor_bin = {0}".format(bin(xor))
	
	ct2num = pt2num^xor
	print 'ct2num = {0}'.format(ct2num)
	print 'ct2num_bin = {0}'.format(bin(ct2num))
	print 'ct2num_hex = {0:02x}'.format(ct2num)
	print '---'
	ct2 += "{0:02x}".format(ct2num)

print ct2
#for n in lst:
	# print n
	

#for i in pt1:
#	sys.stdout.write(str(ord(i)))

