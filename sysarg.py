import sys
print "The number of arguments is %d" % len(sys.argv)
for i in sys.argv:
    print i, sys.argv.index(i)
