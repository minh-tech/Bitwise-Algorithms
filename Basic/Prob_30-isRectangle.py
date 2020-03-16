# Check if given four integers (or sides) make rectangle
# Given four positive integers, determine if there’s a rectangle such that 
# the lengths of its sides are a, b, c and d (in any order).

# Examples :
# Input : 1 1 2 2
# Output : Yes

# Input : 1 2 3 4
# Output : No

def isRectangle(a, b, c, d):
	return not (a ^ b ^ c ^ d)

a, b, c, d = 3, 2, 3, 2
# Expected value True
print(isRectangle(a, b, c, d))

a, b, c, d = 3, 2, 1, 4
# Expected value False
print(isRectangle(a, b, c, d))