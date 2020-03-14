# Count number of bits to be flipped to convert A to B
# Given two numbers ‘a’ and b’. Write a program to count number of bits needed
# to be flipped to convert ‘a’ to ‘b’. 

# Example
# Input : a = 10, b = 20
# Output : 4
# Binary representation of a is 00001010
# Binary representation of b is 00010100
# We need to flip 4 bits in a to make it b.

# Input : a = 7, b = 10
# Output : 3
# Binary representation of a is 00000111
# Binary representation of b is 00001010
# We need to flip 3 bits in a to make it b.

# Check Prob_10-countSetBits.py
def countSetBits(n):
	count = 0
	while n:
		n = n & (n-1)
		count += 1
	return count


def countFlippedBits(a, b):
	# XOR of all elements. Different bits give bit 1
	return countSetBits(a ^ b)


a = 54
b = 81
output = countFlippedBits(a, b)
# Expected value 5
print('Count:', output)