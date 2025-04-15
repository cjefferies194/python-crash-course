responses = ()
polling_active = True
while polling_active:
	place = input('\nWhat is your name?')
	responses = input('What is your dream vacation?')
	polling_active = False

	print('\n----Poll Results----')
	for response in responses:
			print(f'{place} would like to go to {response}.')


