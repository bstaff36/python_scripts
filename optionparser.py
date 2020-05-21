import sys
from optparse import OptionParser

parser = OptionParser(usage='%prog [OPTIONS] "string"')
parser.add_option(
    '-v', '--verbose', type='int', default=0, help='verbosity', dest='verboption')
if (len(sys.argv) == 1):
    parser.print_help()
    sys.exit()
(options, args) = parser.parse_args()

if options.verboption == 9:
    print "dude.. that is really verbose"

print "options are", options
print "args are", args
