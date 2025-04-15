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

def malb(album, song, artist):
	calb = f'{album}{song}{artist}'
	return calb.title

while True:
	print('Please enter an album name, songs, and artists')
	print('Enter q after each time to quit')

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

	malb('aname', 's', 'sartist') 

