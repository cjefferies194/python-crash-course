#6-1
person = {'name':'johnathan', 'age': '34', 'courses': 'none', 'job': 'architect'}
print(person)
#6-2
numbers = {'james': '1', 'john': '3', 'jenefer':'1000000', 'zero':'00000000', 'uknown_user':'10'}
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

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python'}

polls = ['phil', 'jack', 'june', 'jen']
for name in polls:
	if name not in favorite_languages:
		print(f'Take the poll, {name}')
	if name in favorite_languages:
		print(f'Thank you {name}')
	  