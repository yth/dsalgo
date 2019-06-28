def binary_search(sorted_haystack, needle):
	low = 0
	mid = 0
	high = len(sorted_haystack) - 1
	while high >= low:
		mid = (low + high) // 2
		if sorted_haystack[mid] == needle:
			return mid
		elif sorted_haystack[mid] < needle:
			low = mid + 1
		else:
			high = mid - 1
	return -1

if name == "__main__":

	N = map(int, raw_input().split())
	M = int(raw_input())

	print(binary_search(N, M))
