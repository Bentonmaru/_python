import random

user_profession = raw_input("Please enter three professions separated by commas(,) ")

def random_profession(profession):
	myProf = [x.strip() for x in user_profession.split(',')]
	print("We have chosen " + str(random.choice(myProf)) + " for your new profession. Good luck!")

random_profession(user_profession)