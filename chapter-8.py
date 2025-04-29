def display():
	print('This lesson is about functions')

display()


def faverite_book(title):
	print(f'A faverite book of someone is {title}')

faverite_book('(book)')


def tshirt_create(message='print(\'i <3 python\')', size='mens 5', amount='1'):

	print(message, size, amount)


tshirt_create('Trail Life', 'mens 18', '18')
tshirt_create()
tshirt_create('messag', 'mens 2')

def dcity(name, place, fact):
	print(f'{name} is in {place} and is/was/could be/will be ect. {fact}')

dcity('bathroom', 'error file', 'created by a python bug')

def cc(country, city):
	print(f'{city}, {country}')

cc('country', 'city')

def malb():
	calb = f'{album}{song}{artist}'
	return calb.title

while True:
	print('Please enter an album name, songs, and artists')
	print('Enter q to quit')

	album = input('Album name')
	if album == 'q':
		break

	artist = input('Artist')
	if artist == 'q':
		break 

	song = input('Song')
	if song == 'q':
		break

	print(album, artist, song)

malb() 

def show_message():
	Text = []
	while Text != 'X':
		sent = []
		archive = sent
		Text = (input('Enter text here'))
		sent = sent + Text
		print(Text)
	print(archive)
	print(sent)	
show_message()


def sw(toppings):
	tp = []
	while tp != 'X':
		tp = input('Enter sandwich topping')
		toppings = toppings + tp
	print(toppings)
sw('tp')


def bp(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = bp('Colton', 'Jefferies', lives='vicksburg MI', field='coding, yt')

print(user_profile)


def ezpass(epass, model, color, manufacturer, passn, bill,  **info):
	info['epass'] = epass
	info['md'] = model
	info['c'] = color
	info['mf'] = manufacturer
	info['pn'] = passn
	info['$'] = bill
	return info


ezpass_bill = ezpass('none', 'forester', 'light green', 'uknown', 'none', '0.13')
ezpass_bill2 = ezpass('true', 'model t', 'black(luxury)', 'ford', '485630263926', 'none')
ezpass_bill3 = ezpass('none', 'motorwagon', 'white(basic)', 'benz & cie', 'none', '75.12')

print(ezpass_bill)
print(ezpass_bill2)
print(ezpass_bill3)

#8-15 + 8-16 do not work on windows

















