import sys

def count_letters(mystring):
    numeach = {}
    if mystring == "":
    	return numeach
    else:
    	for x in mystring:
    		numeach[x] = mystring.lower().count(x)
    	return numeach

a = count_letters(sys.argv[1])
print(a)