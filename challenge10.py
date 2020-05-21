import sys
import string
arg1=sys.argv[1]

def phoneNumber(arg1):
	mylst = arg1.strip(string.punctuation).split(",")
	print(mylst)
	return ("({}{}{}) {}{}{}-{}{}{}{}".format(mylst[0], mylst[1], mylst[2], mylst[3], mylst[4], mylst[5], mylst[6], mylst[7], mylst[8], mylst[9]))

print(phoneNumber(arg1))