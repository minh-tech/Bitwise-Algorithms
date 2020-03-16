# Swap every two bits in bytes
# Swap all the pair of bits in a byte. Before swapping: 11-10-11-01 After swapping: 11-01-11-10

# Examples:
# Input  : 11 01 00 01
# Output : 11 10 00 10

def swapBitsInPair(x):
	result = 0
	i = 0
	while x:
		# Get 2 last bits
		remain = x & 3
		# If 2 last bits are 01 or 10, invert them.
		if remain in (1, 2):
			remain = remain ^ 3

		# Append those bits in front of result
		result = (remain << (2 * i)) | result
		x = x >> 2
		i += 1
	return result

x = 209 # Binary: 11010001
# Expected value 226. Binary: 11100010
print(swapBitsInPair(x))