# How to turn off a particular bit in a number?
# Given a number n and a value k, turn of the k’th bit in n.
# Input:  n = 15, k = 3
# Binary value of 15 is 1111. Turn off 3th bit. Result is 1011
# Output: 11

def clearBitK(n, k):
	if k <= 0:
		return n

	return n & ~(1 << (k-1))

n = 487
k = 6
# Expected value 455
print(clearBitK(n, k))