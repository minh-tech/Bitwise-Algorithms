# Count set bits in an integer
# Write an efficient program to count number of 1s in binary representation of an integer.
# Input : n = 6
# Output : 2
# Binary representation of 6 is 110 and has 2 set bits

# Input : n = 13
# Output : 3
# Binary representation of 13 is 1101 and has 3 set bits

# My Solution
def countSetBits1(n):
	count = 0
	while n > 0:
		count += n & 1
		n = n >> 1
	return count

# Brian Kernighan’s Algorithm
# The beauty of this solution is the number of times it loops is equal to the number of set bits in a given integer.
def countSetBits2(n):
	count = 0
	while n:
		# Check Prob_05-setRightMostBitZero.py
		n = n & (n-1)
		count += 1
	return count

n = 250
output = countSetBits2(n)
# Expected value 6
print('Count:', output)