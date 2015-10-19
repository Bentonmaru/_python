import time

vehicle = raw_input("Please enter your brand, model, and year(e.g 1993) ")

def parse_string(vehicle):
	brand = vehicle.split()


class Vehicle(object):
	def __init__(self, brand, model, year):
		self.brand = brand
		self.model = model
		self.year = year

	def calculate_age(self, year):
		age = today.year - int(year)
		if age > 10:
			print("$500")
		elif 10 > age > 5:
			print("$1000")
		else:
			print("$2000")

used_vehicle1 = Vehicle(parse_string(vehicle))
used_vehicle1.calculate_age()
