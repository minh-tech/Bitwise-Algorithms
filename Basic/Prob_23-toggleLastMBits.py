# Toggle the last m bits
# Given a non-negative number n. The problem is to toggle the last m bits 
# in the binary representation of n. A toggle operation flips a bit 0 to 1 and a bit 1 to 0

def toggleLastMBits(n, m):
	# calculating a number having 'm' bits and all are set.
	m = (1 << m) - 1
	# Use XOR to toggle bits
	return n ^ m

n = 107
m = 4
# Expected value 100
print(toggleLastMBits(n, m)) 