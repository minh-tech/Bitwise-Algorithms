# Find whether a given number is a power of 4 or not
# Given an integer n, find whether it is a power of 4 or not.
# Example:
# Input : 16
#Output : 16 is a power of 4

#Input : 20
#Output : 20 is not a power of 4

def isPowerOfFour(x):
	while True:
		if x <= 4:
			return x == 4

		# Divide x by 4
		x = x >> 2

# Expected True
print(isPowerOfFour(16))

# Expected False
print(isPowerOfFour(20))

# Expected True
print(isPowerOfFour(64))

# Expected False
print(isPowerOfFour(100))