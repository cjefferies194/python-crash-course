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

food = ['banana', 'apple', 'pineapple']
if 'banana' in food:
	print('Bananas are good')
if 'blueberries' in food:
	print('Blue is for blueberries')
if 'apple' in food:
	print('Appels')
#5-8

users = []
if 'Jaden' in users:
	print('Hello Jaden, would you like to write some code today?')
if 'Admin' in users:
	print('Status is green, little less comments then we would like!')
if 'JJ' in users:
	print('Hello JJ, would you like to write some code today?')
else:
	print('We need to call a meeting as we are out of users')
#5-10

oldusers = ['jonathin', 'jonathan', 'J']
newusers = ['J', 'jonathin', 'joohn']
if newusers in oldusers:
	print('You need to pick a different nickname')

#5-11


digits = ['1', '2', '3', '4', '5' , '6', '7', '8', '9']
if '1' in digits:
	print('1st')
if '2' in digits:
	print('2nd')

if '3' in digits:
	print('3rd')

if '4' in digits:
	print('4th')
if '5' in digits:
	print('5th')

if '6' in digits:
	print('6th')

if '7' in digits:
	print('7th')

if '8' in digits:
	print('8th')

if '9' in digits:
	print('9th')





