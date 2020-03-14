# Add two bit strings
# Given two bit sequences as strings, write a function to return the addition of the two sequences.
# Bit strings can be of different lengths also.
# For example, if string 1 is “1100011” and second string 2 is “10”, then the function should return “1100101”.

def makeEqualLength(a, b):
	lena = len(a)
	lenb = len(b)

	if lena > lenb:
		pad = lena-lenb
		b = pad * '0' + b
	elif lena < lenb:
		pad = lenb-lena
		a = pad * '0' + a
	return a, b

def addBitStrings(a, b):
	a, b = makeEqualLength(a, b)
	carry = 0
	result = ''
	for i in range(len(a)-1, -1, -1):
		bita = int(a[i])
		bitb = int(b[i])
		sum_ = bita ^ bitb ^ carry
		carry = (bita & bitb) | (bita & carry) | (carry & bitb)

		result = str(sum_) + result

	if carry == 1:
		result = 1 + result

	return result

a = '1100011'
b = '10'
sum_ = addBitStrings(a, b)
print(sum_)
