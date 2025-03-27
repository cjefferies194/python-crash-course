# 4-1
pizzas = ['meat lovers','mushroom pizza','hawaiian pizza']
for pizza in pizzas:
	print(f"{pizza.title()} is a pizza.")
print(f'Hawaiian Pizza I do not care for although I am fine with pineapple on pizza.')

# hashtag 4-2
pets = ['hamster','cat','dog','doge']
for pet in pets:		#4-12
	for pet in pets:
		print(f'This is a pet {pet}.')
print(f'This is a meme about a pet: doge')

# exercise three
# numberbutbad = ('won', 'tow', 'twee', 'foor', 'fiev', 'six', 'sevn', 'eht', 'nien', 'ten', 'leven', 'tweelve', 'threeteen', 'foorteen', 'fiveteen', 'six', 'seventween', 'ehteen', 'nienteen', 'tenteen')
for number in range(1,21):
	pass
	# print(number)

# 4-4: Hashtagged for length
# for millions in range (1,1000001):
# 	print(millions)
# print('finished: 115.500 secs')

# 4-5
digits = range(1,1000001)
print(min(digits))
print(max(digits))
print(sum(digits))
# 4-6
for rloop in range(1,20,2):
	print(rloop)
# 4-7
for mult in range (3,30,3):
	print(mult)
# 4-8
for squar in range(1,11):
	square = squar ** 3
	print(square)
# 4-9
squares = [value**3 for value in range(1,11)]
print(squares)
#4-10

here_we_go = ['pizza','meat lovers','mushroom','ice cream']
print('this is pizza')
print(here_we_go[0])
print('this is mac and chees')
print(here_we_go[1])
print('these are tasty... i think')
print(here_we_go[2:4])
#4-11

pizza_friend = pizzas[:]
print(pizza_friend)
pizza_friend.append('pepperoni')
pizzas.append('cheese')
print('i like pizza')
print(pizzas)
print('he likes pizza')
print(pizza_friend)
#4-13

menu = ('mac','cheese','beef','cooked beef','pizza')
for menu in menu:
	print(menu)
menu = ('mac and cheese','cooked beef','pizza')
for menu in menu:
	print(menu)

# 4-14/15
# is the style








