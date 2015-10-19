
class Vehicle(object):
	def __init__(self, brand, model, year):
		self.brand = brand
		self.model = model
		self.year = year

	def calculate_age(self, year):
		age = 2016 - int(year)
		if age > 10:
			print("$500")
		elif 10 > age > 5:
			print("$1000")
		else:
			print("$2000")


used_vehicle1 = Vehicle("Nissan", "Altima", 2016)
used_vehicle1.calculate_age(2016)
