# The function should have one optional argument for length. 
# The default length is 14.

# Generate a password (of given length if provided) that meets the
#  password requirements from Project 1.

# Output: a valid password string


# 1. Password must be at least 14 characters in length
# 2. Password must contain at least one character from each of the following four character sets:
# * Uppercase characters (string.ascii_uppercase)
# * Lowercase characters (string.ascii_lowercase)
# * Numerical Digits (string.digits)
# * Special Characters (string.punctuation)
# 3. Password cannot contain more than three consecutive characters from the same character set.
# 4. Password cannot contain whitespace characters (string.whitespace)

import random
import string

def password_generator(length=14):
	if length < 14:
		length = 14
	randomSource = string.ascii_letters + string.digits + string.punctuation
	password = random.choice(string.ascii_lowercase)
	password += random.choice(string.ascii_uppercase)
	password += random.choice(string.digits)
	password += random.choice(string.punctuation)
	password += random.choice(randomSource)
	i = 6
	while i in range(6, length+1):
		try:
			temp = random.choice(randomSource)
			if check_char_set(temp) != check_char_set(password[-3]):
				password += temp
				i += 1
			else:
				continue
		except KeyboardInterrupt:
			print("User aborted operation.")
	return password
	
def check_char_set(char):
	if char in string.ascii_uppercase:
		return "string.ascii_uppercase"
	elif char in string.ascii_lowercase:
		return "string.ascii_lowercase"
	elif char in string.digits:
		return "string.digits"
	elif char in string.punctuation:
		return "string.punctuation"

if __name__ == '__main__':
	a= password_generator()
	print(a)

