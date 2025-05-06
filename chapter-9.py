class Restaurant:
	def __init__(self, name, type, def1, def2):
		self.name = name
		self.type = type
		self.def1 = def1
		self.def2 = def2
	
	def res_open(self, open):
		if open == 'no':
			print('closed')
		elif open == 'yes':
			print('open')
	def number_served(self, update_served):
		update_served = int(input('How many of you are there'))




restaurant = Restaurant('Bobs Burgers', 'Burgers/Sandwiches', 'family owned', 'very good burgers')
restaurant.res_open('no')
# restaurant.number_served(567)
print(f'Restaurant name is {restaurant.name}')
print(f'Cuisine is {restaurant.type}')
print(f'{restaurant.def1}')
print(f'{restaurant.def2}')


restaurant = Restaurant('Burgers Bobs', 'People/Bob', 'corporation', 'very good people')
restaurant.res_open('yes')

print(f'Restaurant name is {restaurant.name}')
print(f'Cuisine is {restaurant.type}')
print(f'{restaurant.def1}')
print(f'{restaurant.def2}')


restaurant = Restaurant('Why', 'Qs/As', 'if you q we a', 'ask and you shall recieve')
restaurant.res_open('yes')

print(f'Restaurant name is {restaurant.name}')
print(f'Cuisine is {restaurant.type}')
print(f'{restaurant.def1}')
print(f'{restaurant.def2}')


class User:
	def __init__(self, name, nlast):
		self.name = name
		self.nlast = nlast
	
	def pd(self, def1, def2):
		pass
	
	def selfid(self, ID):
		pass
	def privledges(canban, canmute, cansuspend, canchangetext, canuseadmintools):
		if password == Adminofall6540:
			canban = True
			canmute = True
			cansuspend = True
			canchangetext = True
			canuseadmintools = True
	# def login_attempts(self, increment_login_attempts, reset_login_attempts, login, password):
	# 	while login != password:
	# 		login = input('Login')
	# 		if login not password:
	# 			increment_login_attempts + 1
	# 		if increment_login_attempts == 10


user = User('Bob', 'Theodorson')
user.pd('a little fat', 'burger store')
user.selfid('13684265745')

print(f'First name is {user.name}')
print(f'Last name is {user.nlast}')


class IceCreamStand(Restaurant):
	def __init__(self, flavors):
		self.flavors = flavors
		flavors = ('strawberry', 'chocolate', 'vanilla', 'cookiesncream', 'mystery', 'triple fudge masterpiece')


iscream = IceCreamStand('chocolate')	

print(iscream)	


class Car:


	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

		def get_descriptive_name(self):
			long_name = f'{self.year}{self.make}{self.model}'
			return long_name.title()

		def read_odometer(self):
			print(f'this car has {self.odometer_reading} miles on it')

		def update_odometer(self, mileage):
			if mileage >= self.odometer_reading:
				self.odometer_reading = mileage
			else:
				 print('Cant roll back odometer')

		def increment_odometer(self, miles):
			self.odometer_reading += miles


		class ElectricCar(Car):
			def __init__(self, make, model , year):
				super().__init__(make, model, year)



# ULTIMATECAR = ElectricCar('ULTIMATE', 'CAR', '3078')
# print(ULTIMATECAR.get_descriptive_name())


#9-10 - 9-16 doesnt work(windows?)