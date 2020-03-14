# Turn off the rightmost set bit
# Write a program that unsets the rightmost set bit of an integer. 

def clearRightMostBit(x):
	#  n-1 would have all the bits flipped after the rightmost set bit (including the set bit)
	return x & (x - 1)

# x = b'1100'
x = 12

# Expect value 1000
print('{0:b}'.format(clearRightMostBit(12)))