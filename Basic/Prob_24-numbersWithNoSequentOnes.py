# 1 to n bit numbers with no consecutive 1s in binary representation.
# Given a number n, our task is to find all 1 to n bit numbers with no consecutive 1s in their binary representation.

# Examples:
# Input : n = 4
# Output : 1 2 4 5 8 9 10

# Input : n = 3
# Output : 1 2 4 5

def recursion(num, arr, n):

	if num & n == 0:
		arr.append(num)
	else:
		return arr
	
	# Insert 1 only if last digit in num is 0
	if num & 1 == 0:	
		num1 = (num << 1) + 1
		recursion(num1, arr, n)
	
	# Insert 0 if last digit is 1 or 0
	num = num << 1
	recursion(num, arr, n)

	return arr

# Prepare for recursion
def numbersWithNoSequentOnes(n):
	n = 1 << n
	num = 1
	arr = []
	arr = recursion(num, arr, n)
	arr.sort()
	return arr


n = 4
# Expected value [1, 2, 4, 5, 8, 9, 10]
print(numbersWithNoSequentOnes(n))