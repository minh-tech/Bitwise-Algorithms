# Detect if two integers have opposite signs
# Given two signed integers, write a function that returns TRUE if the signs of given integers are DIFFERENT, otherwise FALSE.

def oppositeSigns(x, y):
	# XOR of x and y will give a sign bit as 1 if they have opposite sign
	return (x^y) < 0

# Expected True
print(oppositeSigns(-10, 3))

# Expected False
print(oppositeSigns(10, 3))

# Expected False
print(oppositeSigns(-10, -3))

# Expected True
print(oppositeSigns(10, -3))