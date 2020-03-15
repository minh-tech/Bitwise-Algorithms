# Toggle bits in the given range
# Given a non-negative number n and two values l and r. The problem is to toggle the bits
# in the range l to r in the binary representation of n, to toggle bits from the rightmost 
# lth bit to the rightmost rth bit. A toggle operation flips a bit 0 to 1 and a bit 1 to 0.

# Input : n = 17, l = 2, r = 3
# Output : 23
# 17 => 10001
# 23 => 10111
# The bits in the range 2 to 3 in the binary
# representation of 17 are toggled.

# Input : n = 50, l = 2, r = 5
# Output : 44

def toggleBitsInRange(n, l, r):
	# l = 2, r = 5 => mask = 0011110
	mask = ((1 << r) - 1) - ((1 << (l - 1)) - 1)

	return n ^ mask

n = 50
l = 2
r = 5
# Expected value 44
print(toggleBitsInRange(n, l, r))