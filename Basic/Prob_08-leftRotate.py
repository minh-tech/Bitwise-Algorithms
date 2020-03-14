# Rotate bits of a number
# Bit Rotation: A rotation (or circular shift) is an operation similar to shift 
# except that the bits that fall off at one end are put back to the other end.
# In left rotation, the bits that fall off at left end are put back at right end.
# In right rotation, the bits that fall off at right end are put back at left end.

# Example:
# Let n is stored using 8 bits. Left rotation of n = 11100101 by 3 makes n = 00101111
# Right rotation of n = 11100101 by 3 makes n = 10111100

INT_SIZE = 8

def leftRotate(n, d):
	flag = INT_SIZE
	mask = 1
	while flag > 1:
		mask = (mask << 1) | 1
		flag -= 1

	return n<<d & mask | n>>(INT_SIZE-d)

def rightRotate(n, d):
	flag = INT_SIZE
	mask = 1
	while flag > 1:
		mask = (mask << 1) | 1
		flag -= 1

	return n>>d | n<<(INT_SIZE-d) & mask


n = 234
d = 3

print('The binary    : {0:#0{width}b}'.format(n, width=INT_SIZE+2))

n1 = leftRotate(n, d)
print('Left rotation : {0:#0{width}b}'.format(n1, width=INT_SIZE+2))

n1 = rightRotate(n, d)
print('Right rotation: {0:#0{width}b}'.format(n1, width=INT_SIZE+2))
