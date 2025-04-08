#  5-1
test = 'True'
print(test == 'True')
print(test == 'false')
py = ['java' ,'python', 'bedrock']
pytrue = ['java', 'python']
if py not in pytrue:
	print (f'{py[2]} is not a coding language')

numbers = [107]
if numbers !=108:
	print('Incorrect')

numbers.append(108)
numbers.pop(0)
if numbers == 108:
	print('Correct')
if test.lower() == True:
	print('true')

if numbers[0] <= 102:
	print('Less than')

if numbers[0] >= 102:
	print('Greater than')

if len(numbers):
	print('numbers count:', len(numbers))
	print(numbers[0])

t = ['true']
f = ['false']
if t[0] or f[0]:
	print('true')
else:
	print('false')

if t and not f:
	print('T does not equal F')
else:
	print('T equals F')

if t is f:
	print(id(t))
else:
	print(id(f))

if t == f:
	print('true is false')
else:
	print('that\'s what i thought')

#5-3 - 5-5

alien_colors = ['red', 'blue', 'green']

if 'green' in alien_colors :
	print('Player earned 1 points')
if 'blue' in alien_colors:
	print('Player earned 5 points')
if 'red' in alien_colors:
	print('Player earned 10 points')
else:
	print('Fail, please report this bug')

#5-6
for person in people:
#life = input('How old are you?\n')
life = 1
if life in range(1, 3):
	print('baby')
elif life in range(3, 5):
	print('toddler')
elif life in range(5, 13):
	print ('kid')
elif life in range(13, 18):
	print('teenager')
elif life in range(18, 63):
	print('adult')
elif life in range(63, 131):
	print('elder')
else:
	print('error250')
	raise StopIteration





#5-7

food = ['banana', 'apple', 'pineapple']
if 'banana' in food:
	print('Bananas are good')

if 'blueberries' in food:
	print('Blue is for blueberries')

if 'apple' in food:
	print('Appels')

if 'pineapple' in food:
	print('I also like pineapples')

if 'pineapple' and 'banana' in food:
	print('No putting bananas on pizza!!!!')


#5-8

users = ['Jaden', 'Admin', 'J', 'Jenethen', 'Jon']
for user in users:
	if user == 'Admin':
		print('Hello Admin, would you like to check the reports?')
	else:
		print(f'Hello {user.title()} would you like to write some code today ')






#5-10

oldusers = users
newusers = ['J', 'Admin', 'Jon', 'JoonTheBoi', 'lezgo47']

for nuser in newusers:
	if nuser.lower() in [user.lower() for user in oldusers]:
		print(f'{nuser} has been taken, i am sorry' )
	else:
		print(f'Welcome {nuser}')
#5-11


digits = ['1', '2', '3', '4', '5' , '6', '7', '8', '9']
squares = [int(digit)**2 for digit in digits] 
print(squares)



for digit in digits: 
	if digit == '1':
		print('1st')

	elif '2' == digit:
		print('2nd')

	elif '3' == digit:
		print('3rd')

	else: 
		print(f'{digit}th')







