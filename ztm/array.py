from gettext import find
from operator import contains


class Calory:
	def __init__(self, length=0, data={}):
		self.length = length
		self.data = data

	def get(self, index):
		if self.data:
			return self.data[index]
		return None

	def append(self, item):
		self.data[self.length] = item
		self.length += 1
		return self.length

	def pop(self):
		last_item = self.data[self.length - 1]
		del self.data[self.length - 1]
		self.length -= 1
		return last_item

	def delete(self, index):
		item = self.data[index]
		self.shift_items(index=index)
		return self.data

	def shift_items(self, index):
		for i in range(index, self.length - 1):
			self.data[i] = self.data[i+1]
		del self.data[self.length - 1]
		self.length -= 1
		
	def unshift(self, item):
		self.data[1] = self.data[0]
		self.data[0] = item
		for i in range(1, self.length-1):
			self.data[i + 1] = self.data[i]
		print(self.data, '--->>>')

		return self.data
			
			


if __name__ == '__main__':
	cal = Calory()
	print(cal.get(0))
	cal.append(5)
	cal.append(6)
	print(cal.data)
	# cal.pop()
	# print(cal.delete(0))
	print(cal.unshift(20))
	# print(cal.data)
	# print(cal.length)