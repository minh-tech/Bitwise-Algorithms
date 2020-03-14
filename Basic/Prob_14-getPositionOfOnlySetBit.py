# Find position of the only set bit
# Given a number, return the position of a set bit if only one ‘1’ and all other ’0’s,
# otherwise return -1

def isPowerOfTwo(n):
	# A number n is a power of 2 when bitwise & of n and n-1 will be zero.
	# The expression n&(n-1) will not work when n is 0.
	return n and not (n & (n - 1))

def getPositionOfOnlySetBit(n):

	if not isPowerOfTwo(n):
		return -1

	count = 0
	while n:
		n = n >> 1
		count += 1
	return count

n = 16
# Expected value 5
print(getPositionOfOnlySetBit(n))

n = 12
# Expected value -1
print(getPositionOfOnlySetBit(n))

n = 128
# Expected value 8
print(getPositionOfOnlySetBit(n))