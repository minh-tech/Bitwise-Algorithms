# Find the smallest number with n set and m unset bits
# Given two non-negative numbers n and m. The problem is to find the smallest number
# having n number of set bits and m number of unset bits in its binary representation.

# Input : n = 2, m = 2
# Output : 9
# 9 = 1001
# We can see that in the binary representation of 9 
# there are 2 set and 2 unsets bits and it is the
# smallest number. 

# Input : n = 4, m = 1
# Output : 23

def smallestNumByOnesAndZeros(n, m):
	# n = 4, m = 1 => 10000 + 111 = 10111
	num = (1 << (n + m - 1)) + ((1 << (n - 1)) - 1)

	return num

n = 4
m = 1
# Expected value 23
ans = smallestNumByOnesAndZeros(n, m)
print (ans)