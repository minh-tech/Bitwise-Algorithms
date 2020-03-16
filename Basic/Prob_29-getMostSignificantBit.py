# Find most significant set bit of a number
# Given a number, find the most significant bit number which is set bit and which is in power of two

# Examples:
# Input : 10
# Output : 8
# Binary representation of 10 is 1010
# The most significant bit corresponds
# to decimal number 8.

# Input : 18
# Output : 16

# An efficient solution is to one by one set bits, then add 1 so that only the bit after MSB is set.
#Finally right shift by 1 and return the answer.
def getMostSignificantBit(n):
	i = 0
	while n & (n+1) != 0:
		# This will repeat until all bits of n is set (Ex: 1010 => 1111)
		n |= n >> (1<<i)
		i += 1
	
	return (n+1)>>1

n = 273 # Binary: 100010001
# Expected value 256. Binary: 100000000
print(getMostSignificantBit(n))