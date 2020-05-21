import sys
arg1 = sys.argv[1]

def myfunc(arg1):
	"""return first char that is not repeated in the string
	ignore case when counting but return original char.

	if all repeating, return empty string.
	"""
	check = ""
	for char in arg1:
		if arg1.lower().count(char.lower()) == 1:
			check = char
			break
	return check

print(myfunc(arg1))