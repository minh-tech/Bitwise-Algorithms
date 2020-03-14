# Find the element that appears once
# Given an array where every element occurs THREE times, except one element which occurs only ONCE.
# Find the element that occurs ONCE. Expected time complexity is O(n) and O(1) extra space.

# Examples :
# Input: arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
# Output: 2
# In the given array all element appear three times except 2 which appears once.

# Input: arr = [10, 20, 10, 30, 10, 30, 30]
# Output: 20

def getSingle(arr, debug=False):
	first = 0
	second = 0

	for elm in arr:
		if debug:
			print('element: {0:b}'.format(elm))
		
		second |= (first & elm)
		# (first & elm) gives the bits that are there in both 'first' and new element from arr.
		# We add these bits to 'second' using bitwise OR 
		if debug:
			print('second: {0:b}'.format(second))

		first ^= elm
		# XOR the new bits with previous 'first' to get all bits appearing odd number of times
		if debug:
			print('first: {0:b}'.format(first))

		common_bit_mask = ~(first & second)
		# The common bits are those bits which appear third time.
		# So these bits should not be in both 'first' and 'second'.  
        # common_bit_mask contains all these bits as 0, so that the bits can be removed from 'first' and 'second'
		if debug:
			print('common_bit_mask: {0:b}'.format(~common_bit_mask))

		first &= common_bit_mask
		# Remove common bits (the bits that appear third time) from 'first'
		if debug:
			print('first: {0:b}'.format(first))

		second &= common_bit_mask
		# Remove common bits (the bits that appear third time) from 'second'
		if debug:
			print('second: {0:b}'.format(second))
			print('-----------------------------')
	return first


arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]

single = getSingle(arr)
print('The single number:', single)
