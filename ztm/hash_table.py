class DictTable:
	data = []

	def __init__(self, size):
		self.data = list(range(size))

	def _hash(self, key):
		hash_num = 0
		for i in range(len(key)):
			hash_num = (hash_num + ord(key[i]) * i) % len(self.data)
		return hash_num

	def set(self, key, value):
		print(key)
		address = self._hash(key)
		print(address)
		if not self.data[address]:
			self.data[address] = []
			print(self.data)
		self.data[address].append([key, value])
		return self.data


if __name__ == '__main__':
	hash_table = DictTable(4)
	hash_table.set('oranges', 1000)
