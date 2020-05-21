# 1. Password must be at least 14 characters in length
# 2. Password must contain at least one character from each of the following four character sets:
# * Uppercase characters (string.ascii_uppercase)
# * Lowercase characters (string.ascii_lowercase)
# * Numerical Digits (string.digits)
# * Special Characters (string.punctuation)
# 3. Password cannot contain more than three consecutive characters from the same character set.
# 4. Password cannot contain whitespace characters (string.whitespace)
# 5. Returns True if a valid password. False, otherwise.
import string

def password_checker(mystring):
	if len(mystring) < 14:
		return False
	upper = False
	lower = False
	digit = False
	punc = False
	for char in mystring:
		if char in string.whitespace:
			return False
		elif char in string.ascii_lowercase:
			lower = True
		elif char in string.ascii_uppercase:
			upper = True
		elif char in string.digits:
			digit = True
		elif char in string.punctuation:
			punc = True
	if (upper and lower and digit and punc) == False:
		return False
	# range(4, len(mystring)+1):
	for i in range(3, len(mystring)):
		this = check_char_set(mystring[i])
		pasta = check_char_set(mystring[i-1])
		pastb = check_char_set(mystring[i-2])
		pastc = check_char_set(mystring[i-3])
		if this == pasta == pastb == pastc:
			return False
	return True 
				
def check_char_set(char):
	if char in string.ascii_uppercase:
		return "string.ascii_uppercase"
	elif char in string.ascii_lowercase:
		return "string.ascii_lowercase"
	elif char in string.digits:
		return "string.digits"
	elif char in string.punctuation:
		return "string.punctuation"