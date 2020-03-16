# Sum of numbers with exactly 2 bits set
 # Given a number n. Find sum of all number upto n whose 2 bits are set.

# Input : 10
# Output : 33
# 3 + 5 + 6 + 9 + 10 = 33

# Input : 100
# Output : 762

def findSumBy2BitsNum(n):
	num1 = 1
	sum_ = 0
	while num1 < n:
		num1 = num1 << 1
		num2 = 1
		while (num1 | num2) <= n and num1 != num2:
			sum_ = sum_ + (num1 | num2)
			num2 = num2 << 1
	return sum_

n = 100
# Expected value 762
print(findSumBy2BitsNum(n))

# How does it work?
# The number whose 2 bits are set is of the form 2^x + 2^y and this number 
# is less then n. So we have to find only numbers in the range upto n which 
# is of form 2^i + 2^j where 2^i | 2^j <= n