#6-1 + 6-7
person = {'name':'johnathan', 'age': '34', 'courses': 'none', 'job': 'architect'}
person2 = {'name':'june', 'age':'13','courses':'middle school', 'job':'none'}
person3 = {'name':'john', 'age':'76','courses':'none', 'job':'retired'}
people = [person, person2, person3]
for people in people:
	print(people)
#6-2 + 6-10
numbers = {'james': ['1', '30'], 'john': ['3', '3'], 'jenefer':['1000000', '0'], 'zero':['00000000', '0'], 'uknown_user':['10', 'idk']}
print(numbers)
#6-3
datatypes = {'dictionary': 'string holder', 'list': 'string holder', 'tuple':'unchangeable string holder',
'int': 'number', 'str': 'words typed'}
print(datatypes)
#6-4
for key, value in datatypes.items():
	print(f'key:{key}')
	print(f'value: {value}')
#6-5
rivers = {'nile': 'egypt', 'mississippi': 'america', 'rhine': 'germany'}
for river in rivers:
	print(river)
for country in rivers.values():
	print(country)
#6-6

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}

polls = ['phil', 'jack', 'june', 'jen']
for name in polls:
	if name not in favorite_languages:
		print(f'Take the poll, {name}')
	if name in favorite_languages:
		print(f'Thank you {name}')
#6-8

pet1 = {'name':'jerry', 'kind':'hamster', 'owner':'john', 'desc': 'is a stinky boy'}
pet2 = {'name':'dune', 'kind':'cat', 'owner':'johnathan', 'desc': 'is at least civilized'}
pet3 = {'name':'doofus', 'kind':'dog', 'owner':'june', 'desc': 'is a straight up idiot'}
pets = [pet1, pet2, pet3]
for pet in pets:
	print(f'{pet['name'].title()} {pet['desc']} and is a {pet['kind']} owned by {pet['owner'].title()}.')

#6-9



fave_places = {'John':['The Czech Republic', 'Slovakia'], 'June':['Turkey', 'Italy', 'France'], 'Johnathan':['Switzerland', 'Estonia']}
# join syntax: `string`.join(`iterable`)
for name, countries in fave_places.items():
	print(f'{name}\'s favorite places are {','.join(countries[:-1])}, and {countries[-1]}')

#6-11

cities = {
	'Atlanta': {
		'place':'America',
 		'population':'510,832',
 		'fact':'the city in the forest'
 	},
  	'Khartoum':{ 
  		'place':'Sudan',
 		'population':'6,300,000',
  		'fact':'named elephants trunk'
  	},
  	'Berlin': {
  		'place':'Germany',
 		'population':'3,780,000',
  		'fact':'9x bigger than Paris'
	}
}
for key, value in cities.items():
	print(f'{key} is in {value['place']}, is {value['fact']}, with a population of {value['population']}')


	  