#  5-1
test = 'True'
print(test == 'True')
print(test == 'false')
py = ['java' ,'python', 'bedrock']
pytrue = ['java', 'python']
if py not in pytrue:
	print (f'{py[2]} is not a coding language')
number = ['107']
if number !=108:
	print('Incorrect')
number.append(108)
number.pop(0)
if number := 108:
	print('Correct')
#5-3 - 5-5
buff = 'small', 'medium', 'large', 'huge'
small = 'small'
medium = 'medium'
large = 'large'
huge = 'huge'
if buff := small:
	print('1')
elif buff := medium:
	print('5')
elif buff := large:
	print('10')
elif buff := huge:
	print('1')
else:
	print('Fail, please report this bug')
#5-6
username = 'Dan'
play = '1'
if play := '1':
	print('Adventurer', username)
elif play := '10':
	print('Knight', username)
elif play := '20':
	print('King',)
elif play := '50':
	print('Overlord', username)
elif play := '100':
	print('Siegemaster', username)
else:
	print('Lord', username) 
#5-7