import re
import urllib
import urllib2
import sys
from optparse import OptionParser

parser = OptionParser(usage='%prog --url http://127.0.0.1/contact.html')
parser.add_option('-u', '--url', default='http://127.0.0.1/contact.html',
                  help='Enter a target url', dest='url')

(options, args) = parser.parse_args()

try:
    content = urllib2.urlopen(options.url).read()
except:
    print "Error Accessing website"
    sys.exit(2)

result = re.findall(
    r"([\w\+\-\.]+@[0-9a-zA-Z][.-0-9a-zA-Z]*.[a-zA-Z]+).*?(\d{3}).?(\d{3}).?(\d{4})", content)
for addr, ph1, ph2, ph3 in result:
    print "Contact found! Email: {0:<}\n               Phone: %s-%s-%s".format(addr) % (ph1, ph2, ph3)
