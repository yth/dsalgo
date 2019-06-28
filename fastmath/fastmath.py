def even(a):
	return a % 2 == 0

def mul(a, b):
	def mult(a, b, c):
		if a == 1:
			return b + c
		elif even(a):
			return mult(a//2, b*2, c)
		else:
			a -= 1
			c += b
			return mult(a, b, c)

	return mult(a, b, 0)

def pow(b, p):

	if b == 1:
		return 1

	def powr(b, p, c):
		if p == 1:
			return b * c
		elif even(p):
			return powr(b ** 2, p//2, c)
		else:
			p -= 1
			c *= b
			return powr(b, p, c)

	return powr(b, p, 1)
		

if __name__ == "__main__":

	import sys

	# sys.setrecursionlimit(10000)

	# print("start")
	print(mul(9, 9))
	print(mul(999, 999))

	print(pow(1, 10))
	print(pow(2, 10))