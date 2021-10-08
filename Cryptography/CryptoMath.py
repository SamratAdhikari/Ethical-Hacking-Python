# CryptoMath Module


def gcd(a, b):
	# return the GCD of a and b using Euclid's algorithm
	while a != 0:
		a, b = b % a, a
	return b


def findModInverse(a, b):
	# Return the modular inverse of a % m, which is the number x such that a*x % m = 1
	if gcd(a, b) != 1:
		return None # no mod inverse if a and m arent relatively prime
		
	# Calculate using the extended Euclidean algorithm
	u1, u2, u3 = 1, 0, a
	v1, v2, v3 = 0, 1, b
	while v3 != 0:
		q = u3 // v3 
		v1, v2, v3, u1, u2, u3 = (u1-q*v1), (u2-q*v2), (u3-q*v3), v1, v2, v3

	return u1 % b


if __name__ == "__main__":
	print(findModInverse(7, 26))
	print(gcd(2, 5))

