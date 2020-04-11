def main():
	x = 5
	print(f'id of x is {id(x)}')
	kitten(x)
	print(f'in main: x is {x}')
	main2()

def kitten(a):
	print(f'id of a is {id(a)}')
	a = 3
	print(f'id of new a is {id(a)}')
	print('Meow')
	print(a)

### Integers are immutable. When x is passed to kitten, a copy of it is
### actually passed, and hence x and a have the same ID number. When a
### is assigned the integer 3, it creates a new veriable, and so the ID
### number changes, and the value of x in main does not. Lists are mutable,
### however. If a list is changed in kitten, it will also change in main:

def main2():
	print('--------------------')
	x = [5]
	print(f'id of x is {id(x)}')
	kitten2(x)
	print(f'in main2: x is {x}')

def kitten2(a):
	print(f'id of a is {id(a)}')
	a[0] = 3
	print(f'id of new a is {id(a)}')
	print('Meow2')
	print(a)

if __name__ == '__main__':
	main()