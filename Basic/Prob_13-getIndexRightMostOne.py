
# Check Prob_11-countFlippedBits.py
def countSetBits(n):
	count = 0
	while n:
		n = n & (n-1)
		count += 1
	return count

def getIndexRightMostOne(n):

	return countSetBits(n ^ (n-1))

n = 19

print(getIndexRightMostOne(n))

