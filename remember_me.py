# Refactoring previous code using functions
import json 

def Greet_User():
	'''Greet the user by name'''

	filename = 'username.json'
	try: 
		with open(filename) as f_obj:
			username = json.load()
	except FileNotFoundError:
		username = input('What is your name?')
		with open(filename) as f_obj:
			json.dump(username, f_obj)
			print('We will remeber you when you come back, ' + username + '!')
	else:
		print('Welcome back, ' + username + '!')

# Calling the function 
Greet_User()

''' 
The rest of the chapter explains how breaking the above function down 
even further, into the parts, checking for a stored name, getting a new
username, and finally greeting the user, will ease future program writing. 

Im going to end up practicing this refactoring in the following 
final exercises for this chapter, so, yea Im just going to leave this 
function as is, for now. 
'''