# Set the rightmost unset bit
# Given a non-negative number n. The problem is to set the rightmost unset bit 
# in the binary representation of n. If there are no unset bits, then just leave the number as it is.

def setRightmostUnsetBit(x):

	# # if all bits of 'n' are set 
	if x & (x + 1) == 0:
		return x

	return x | (x + 1)

n = 21
# Expected value 23
print(setRightmostUnsetBit(n))