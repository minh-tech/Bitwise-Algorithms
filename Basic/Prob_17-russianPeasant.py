# Russian Peasant (Multiply two numbers using bitwise operators)
# Given two integers, write a function to multiply them using Russian peasant algorithm.
# The idea is to double the first number and halve the second number repeatedly till 
# the second number becomes 1. In the process, whenever the second number become odd, 
# we add the first number to result (result is initialized as 0)

def russianPeasant(a, b):

	result = 0
	while b >= 1:
		# Check odd number
		if b & 1:
			result += a

		a <<= 1
		b >>= 1

	return result

# Expected value 38
print(russianPeasant(38, 1))

# Expected value 391
print(russianPeasant(23, 17))

# Expected value 400
print(russianPeasant(25, 16))

