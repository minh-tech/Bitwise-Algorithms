# Calculate XOR from 1 to n.
# Given a number n, the task is to find the XOR from 1 to n.
# Examples :

# Input : n = 6
# Output : 7
# 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6  = 7

# Input : n = 7
# Output : 0
# 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 = 0

def computeXORFrom1(n):

	# n & 3 equivalent to n % 4 but less expensive on most of computers	
	if n & 3 == 0:
		return n

	if n & 3 == 1:
		return 1

	if n & 3 == 2:
		return n+1

	#if n & 3 == 3:
	return 0

n = 14
# Expected value 15
print(computeXORFrom1(n))

# How does this work?
# Number Binary-Repr  XOR-from-1-to-n
# 1         1           [0001]
# 2        10           [0011]
# 3        11           [0000]  <----- We get a 0
# 4       100           [0100]  <----- Equals to n
# 5       101           [0001]
# 6       110           [0111]
# 7       111           [0000]  <----- We get 0
# 8      1000           [1000]  <----- Equals to n
# 9      1001           [0001]
# 10     1010           [1011]
# 11     1011           [0000] <------ We get 0
# 12     1100           [1100] <------ Equals to n