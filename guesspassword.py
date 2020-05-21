def guesspassword(pwguess):
    pd = urllib.urlencode({'username': 'admin', 'password': pwguess})
    try:
        content = urllib2.urlopen('http://127.0.0.1/login.php', pd).read()
    except (urllib2.URLError, urllib2.HTTPError):
        print "Error accessing page"
        content = ''
    return "success" in content.lower()
