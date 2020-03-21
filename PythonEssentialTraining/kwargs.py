def main():
	kitten(Buffy='meow', Zilla='grr', Angel='rawr')

def kitten(**kwargs):
	if len(kwargs):
		for k in kwargs:
			print(f'Kitten {k} says {kwargs[k]}')