# Add 1 to a given number
# Write a program to add 1 to a given number. The use of operators like ‘+’, ‘-‘, ‘*’, ‘/’, ‘++’, ‘–‘ …etc are not allowed.

def addOne(x):
	# ~x = -(x + 1) [~ is for bitwise complement]
	# (x + 1) is due to addition of 1 in 2’s complement conversion
	# To get (x + 1) apply negation once again.
	return -(~x)

# Expected 13
print(addOne(12))
