# Convert a binary number to octal
# The problem is to convert the given binary number (represented as string) 
# to its equivalent octal number. The input could be very large and may not fit even into unsigned long long int.

# Examples:
# Input : 110001110
# Output : 616

# Input  : 1111001010010100001.01011011001101101
# Output : 1712241.266332

# Create a Binary to Octal hash map
def createBinToOctMap():
	binToOctMap = dict()
	binToOctMap['000'] = '0'
	binToOctMap['001'] = '1'
	binToOctMap['010'] = '2'
	binToOctMap['011'] = '3'
	binToOctMap['100'] = '4'
	binToOctMap['101'] = '5'
	binToOctMap['110'] = '6'
	binToOctMap['111'] = '7'
	return binToOctMap

# Padding zeros before or after the string
def paddingZeros(string, pos='pre'):
	length = len(string)
	remain = length % 3
	zeros = 3 - remain if remain else 0
	if pos == 'pre':
		return '0' * zeros + string
	else:
		return string + '0' * zeros

# Convert binary to octal
def convertBinToOct(bin):

	binToOctMap = createBinToOctMap()
	dotInx = bin.index('.')
	newBin = bin[dotInx+1:]
	newBin = paddingZeros(bin[:dotInx], pos='pre') + '.' + paddingZeros(newBin, pos='post')
	
	i = 0
	octa = ''
	while i < len(newBin):

		if newBin[i] == '.':
			octa = octa + '.'
			i += 1
		
		triBits = newBin[i:i+3]
		octa = octa + binToOctMap[triBits]
		i += 3
	
	return octa


bin = '1111001010010100001.01011011001101101'
# Expected value 1712241.266332
print(convertBinToOct(bin))