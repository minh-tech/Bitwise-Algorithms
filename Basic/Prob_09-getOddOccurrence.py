# Find the Number Occurring Odd Number of Times
# Given an array of positive integers. All numbers occur even number of times
# except one number which occurs odd number of times. Find the number in O(n) time & constant space.

# Examples :
# Input : arr = {1, 2, 3, 2, 3, 1, 3}
# Output : 3

# Input : arr = {5, 7, 2, 7, 5, 2, 5}
# Output : 5

def getOddOccurrence(arr):
	result = 0
	for elm in arr:
		# XOR of all elements give odd ocurring element
		result = result ^ elm
	return result

arr = [1, 2, 3, 2, 3, 1, 3]
number = getOddOccurrence(arr)
# Expected value 3
print('The number:', number)

arr = [5, 7, 2, 7, 5, 2, 5]
number = getOddOccurrence(arr)
# Expected value 5
print('The number:', number)