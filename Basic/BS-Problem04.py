# Multiply a given Integer with 3.5
# Given a integer x, write a function that multiplies x with 3.5 and returns the integer result. You are not allowed to use %, /, *. 

def multiplyWith3Point5(x):
	# Convert to (8*x – x)/2. to calculate 8*x, left shift x by 3 and to calculate x/2, right shift x by 1
	return ((x << 3) - x) >> 1

x = 5
# Expected 17
print(multiplyWith3Point5(x))