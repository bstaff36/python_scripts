from PIL import Image
from PIL.ExifTags import TAGS
from optparse import OptionParser
import glob
import sys
import os

parser = OptionParser(usage='%prog <directory of images>')

(options, args) = parser.parse_args()
if len(args) == 0:
    parser.print_help()
    sys.exit(2)

if not os.path.exists(args[0]):
    print "Directory doesn't exist"
    sys.exit(2)

listoffiles = glob.glob(args[0] + "*.jpg")
for file in listoffiles:
    try:
        imageobject = Image.open(file)
        imageobject.thumbnail((100, 100), Image.ANTIALIAS)
        imageobject.show()
    except Exception as e:
        print "An exception occured." + str(e)
