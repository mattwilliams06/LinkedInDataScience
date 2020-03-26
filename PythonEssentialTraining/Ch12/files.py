# def main():
# 	f = open('lines.txt', 'r')
# 	for line in f:
# 		print(line.rstrip())
# 	f.close()

def main():
	with open('lines.txt', 'r') as f:
		for line in f:
			print(line.rstrip())

if __name__ == '__main__':
	main()