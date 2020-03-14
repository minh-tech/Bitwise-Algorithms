# Position of rightmost set bit
# Write a one line function to return position of first 1 from right to left,
# in binary representation of an Integer.

# Example
# Input : 18
# Binary Representation 010010
# Output: 2

# Input : 19
# Binary Representation 010011
# Output: 1


# Check Prob_11-countFlippedBits.py
def countSetBits(n):
	count = 0
	while n:
		n = n & (n-1)
		count += 1
	return count


def getPositionOfRightMostSetBit(n):
	# XOR of all elements. Different bits give bit 1
	return countSetBits(n ^ (n-1))

# Binary 101110000
n = 368
# Expected value 5
print(getPositionOfRightMostSetBit(n))

