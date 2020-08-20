import os

while True:
	os.system('clear')
	name = input('Enter your name: ')
	if name == '' or name is None:
          break
	print(f'Hello {name}')
