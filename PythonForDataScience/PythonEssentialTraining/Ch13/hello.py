s = 'Hello, World.'
# print the string itself
print(repr(s))

class bunny:
	def __init__(self, n):
		self._n = n


s = bunny(47)
print(s)
# The above displays a bunny object and memory location.
# This is not particularly useful, so that's where the
# representation comes in.
class new_bunny:
	def __init__(self, n):
		self._n = n
	def __repr__(self):
		return f'repr: The number of bunnies is {self._n}'
	def __str__(self):
		return f'str: The number of bunnies is {self._n}'

s = new_bunny(32)
print(s)
print(repr(s))