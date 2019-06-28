def fib(n):
	def fib_iter(a, b, counter):
		if counter < 2:
			return a
		else:
			return fib_iter(a + b, a, counter - 1)

	return fib_iter(1, 1, n-1)

if __name__ == "__main__":

	print(fib(1))
	print(fib(2))
	print(fib(3))