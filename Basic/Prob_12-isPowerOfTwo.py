# Program to find whether a no is power of two
# Given a positive integer, write a function to find if it is a power of two or not.

# Examples :

# Input : n = 32
# Output : Yes
# 2^5 = 32

# Input : n = 7
# Output : No


def isPowerOfTwo(n):
	# A number n is a power of 2 when bitwise & of n and n-1 will be zero.
	# The expression n&(n-1) will not work when n is 0.
	return n and not (n & (n - 1))

# Expcted False
print(isPowerOfTwo(61))
# Expected True
print(isPowerOfTwo(128))
