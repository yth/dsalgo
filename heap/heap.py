class minHeap:
	def __init__(self):
		self.heap = []
		self.dict = {}
		self.size = 0

	def __str__(self):
		s = "{\n"

		for x in range(self.size):
			s += "\t"
			s += str(x)
			s += " : "
			s += str(self.heap[x])
			s += "\n"

		s += "}"

		return s

	def _parent(self, index):
		return max((index-1) // 2, 0)

	def _lchild(self, index):
		return (index << 1) + 1

	def _rchild(self, index):
		return self._lchild(index) + 1

	def _min_child(self, index):
		lchild_index = self._lchild(index)
		rchild_index = lchild_index + 1

		if lchild_index >= self.size:
			return -1

		if rchild_index < self.size:
			min_child_index = lchild_index \
				if self.heap[lchild_index] < self.heap[rchild_index] \
				else rchild_index

			return min_child_index \
				if self.heap[min_child_index] < self.heap[index] \
				else -1

		return lchild_index \
			if self.heap[lchild_index] < self.heap[index] \
			else -1

	def _swap(self, i1, i2):
		self.dict[self.heap[i1]] = i2
		self.dict[self.heap[i2]] = i1

		self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]

	def _bubble_up(self, index):
		parent_index = self._parent(index)
		while self.heap[index] < self.heap[parent_index]:
			self._swap(index, parent_index)
			index = parent_index
			parent_index = self._parent(index)

	def _bubble_down(self, index):
		min_child_index = self._min_child(index)
		if min_child_index != -1:
			self._swap(index, min_child_index)
			self._bubble_down(min_child_index)

	def _is_heap(self):
		for x in range(1, size, 1):
			if not (h.heap[x] >= h.heap[h._parent(x)]):
				print("Failure!")
				return
		print("Success!")

	def insert(self, new_item):
		self.heap.append(new_item)
		self.dict[new_item] = self.size
		self._bubble_up(self.size)
		self.size += 1

	def peek(self):
		return self.heap[0]

	def delete_min(self):
		self._swap(0, self.size-1)
		min_value = self.heap.pop(self.size-1)
		self.size -= 1
		del(self.dict[min_value])

		if self.size > 1:
			self._bubble_down(0)

		return min_value

	def decrease_key(self, old, new):
		if old not in self.dict:
			return

		if old < new:
			return
		index = self.dict[old]
		del(self.dict[old])
		self.dict[new] = index
		self.heap[index] = new
		self._bubble_up(index)

if __name__ == "__main__":
	h = minHeap()
	size = 10
	for x in range(size, 0, -1):
		h.insert(x)

	h._is_heap()


	l = []
	while h.size > 0:
		l.append(h.delete_min())

	for x in range(1, len(l)):
		assert(l[x-1] <= l[x])

	print("Success!")


	for x in range(size, 0, -1):
		h.insert(x)

	h.decrease_key(size, 0)

	for x in range(1, size, 1):
		assert(h.heap[x] >= h.heap[h._parent(x)])

	print("Success!")


	l = []
	while h.size > 0:
		l.append(h.delete_min())

	for x in range(1, len(l)):
		assert(l[x-1] < l[x])

	print("Success!")