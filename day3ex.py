# Print table of Octal, Decimal, Binary, and Chars for 63-72

# print("{0:>5s}{1:>12s}{2:>8}{3:>10}{4:>8}".format("Octal","Decimal","Hex","Bin","Char"))
# print("{0}".format(("-")*43))
# for i in range(63,73):
# 	print("{0:>#5o}{1:>12}{2:>#8x}{3:10b}{4:8c}".format(i,i,i,i,i))



''' Section 5 Daily Exercise: Pull in a file, read it, format it, and write back out to a new file. The infile is chaotic and contains several fields about employees. The outfile should contain a dictionary with employee IDs as keys and Employee info as values. Employee info should be a dictionary containing firstname, lastname, and phone number as keys.'''

import re
d={}
outfile=open("moreimportant.txt",'w')
with open("important.txt") as f:
	texts = f.read()
	new = re.sub('\s+'," ", texts)   #substitute all the excess spaces with a single space
	''' Now I turned the text into a list of employees. regex sorted for pattern 2 digits + " " + 1 or more letters + ":" + 1 or more letters + ":" + phone number.
	phone number format is: 0-1 "(" + 3 digits + 0-1 ")" + possible separator (-/_ ) + 3 digits + separator + 4 digits'''
	newnew = re.findall("\d*\s[a-zA-Z]*:[a-zA-Z]*:\(?\d{3}\)?[/_\s-]?\d{3}[/_\s-]?\d{4}", new)
	# I ran through the list and for each employee I had re.search separate the information into groups that I could reference.
	# Group 1 is employee ID, 2 is Firstname, 3is Lastname, 4 is phone number
	for i in newnew:
		match = re.search("(\d*\s)([a-zA-Z]*):([a-zA-Z]*):(\(?\d{3}\)?[/_\s-]?\d{3}[/_\s-]?\d{4})", i)
		# Because the phone number format is not standardized, I did an re.findall to pull each digit and then I joined then together
		temp = re.findall("\d",match.group(4))
		nums = "".join("{}{}{}-{}{}{}-{}{}{}{}".format(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9]))
		# finally, smash all that into a dict of dicts
		d[match.group(1)] = {"firstname": match.group(2), "lastname":match.group(3), "phone number": nums}
	outfile.write(str(d))	#write our cleaned up dictionary to the new file			

print(new)
print()
print(newnew)
print()
print(match)
print()
print(d)
