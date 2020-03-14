# Equal Sum and XOR
# Given a positive integer n, find count of positive integers i in range(0, n) and n+i = n^i

# Input n = 12
# Output: 4
# 12^i = 12+i hold only for i = 0, 1, 2, 3

def countValueSumAndXOR(n):
	count = 1
	while n:
		if not n & 1:
			count = count << 1
		n = n >> 1

	return count


n = 100
print(countValueSumAndXOR(n))

# How does this work?
# n + i = n ^ i implies n & i = 0
# Hence our problem reduces to finding values of i such that n & i = 0.
# We can use the count of unset-bits in the binary representation of n.
# Hence, total such combinations are 2^(count of unset bits in n)