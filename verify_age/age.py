age = int(raw_input("Please enter your age in order to access out website: "))

def verify_age(age):
	if age > 18:
		print("Welcome to our website")
	else:
		print("You are not old enough to visit our website, may I suggest something else?")
		 
	return

verify_age(age)