# level 1: http://www.pythonchallenge.com/pc/def/map.html
# # shift alphabet to right 2 chars and decode:

# strs = 'abcdefghijklmnopqrstuvwxyz'      
# def shifttext(shift):
# 	inp = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# 	data = []
# 	for i in inp:                     
# 	    if i.strip() and i in strs:              
# 	        data.append(strs[(strs.index(i) + shift) % 26])    
# 	    else:
# 	        data.append(i)           
# 	output = ''.join(data)
# 	print(output)
# shifttext(2)
# solution: http://wiki.pythonchallenge.com/index.php?title=Level1:Main_Page



# level 2: http://www.pythonchallenge.com/pc/def/ocr.html
# import string
# with open("test.txt") as f:
# 	infile = f.read()
# 	nextfile = ' '.join(word.strip(string.punctuation) for word in infile.split())
# 	print(nextfile)



level3: http://www.pythonchallenge.com/pc/def/equality.html
