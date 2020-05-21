import sys
import string

arg1 = sys.argv[1]
def textReader(arg1):
	myfile = open(arg1, "r")
	infile = myfile.read()
	numeach = {}
	for x in string.ascii_lowercase:
	   numeach[x] = infile.lower().count(x)
	# del numeach[" "]
	char_occurence = max(numeach.values())
	common_char = list(numeach.keys())[list(numeach.values()).index(char_occurence)]

	nextfile = ' '.join(word.strip(string.punctuation) for word in infile.split())
	split_file = nextfile.lower().split()
	counter = split_file.count('the') 
	wordcount = len(split_file)

	print("%s is the most common letter. It occurs %s times." %(common_char.upper(), char_occurence))
	print(int((counter/wordcount)*100)//1)

	with open("challenge8_output.txt", "w+") as f:
		with open(arg1, "r") as g:
			count = 0
			y = []
			for line in g:
				z= line.split()
				y += z
				count = len(y)
				if count >= 10:
					x = " ".join(y[:10])
					f.write(x)
					print(x)
					f.close()
					break

textReader(arg1)
