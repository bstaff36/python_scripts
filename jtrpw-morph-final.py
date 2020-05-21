def reverseword(word):
    # This function takes in a word and returns the word in reverse
    return word[::-1]


def leetspeak(word):
    # This function takes in a word and returns a "leet speak" version of the
    # word
    return word.replace('a', '4').replace('e', '3').replace('L', '1').replace('S', '5')


def appendnumbers(word):
    # This function takes in a word and returns a list of 100 words with
    # digits 0-99 appended
    newlist = []
    for a in range(100):
        newlist.append("%s%02d" % (word, a))
    return newlist

file = open('/usr/share/john/password.lst', 'r')

listoflines = file.readlines()
for password in listoflines:
    word = password.strip()
    print word
    print reverseword(word)
    print leetspeak(word)
    for a in appendnumbers(word):
        print a

file.close()
