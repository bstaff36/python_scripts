# Copyright 2015 Mark Baggett - Driftnet scapy
# for exclusive use with Mark Baggett's Python Course

from imagelib import *
import argparse

# Define and parse all the command line options

parser=argparse.ArgumentParser()
parser.add_argument('-w','--write',required=False,help='Write images to the supplied directory',dest='directory')
parser.add_argument('-d','--display',action='store_true',required=False,help='Display the options')
parser.add_argument('-m','--maps',action='store_true',required=False,help='Print google maps links')
parser.add_argument('-e','--exif',action='store_true',required=False,help='Display the exif data')
parser.add_argument('-v','--verbose',action='store_true',required=False,help='Produce Verbose Output')
parser.add_argument('packet_capture',help='A PCAP file containing images.')
args=parser.parse_args()

if not os.path.exists(args.packet_capture):
    print "PCAP file does not exist."
    sys.exit(2)

# First lets read the packets we are interested in using read_filtered_packets
if args.verbose:
    print "Processing...(This could take a while)"

all_packets = read_filtered_packets(args.packet_capture)
imagenumber=1
for eachp in all_packets.sessions().values():
    stream_images = http_stream_to_images(eachp)
    if len(stream_images) == 0:
        continue
    for each_image in stream_images:
        try:
        # if the -d option was specified then display the image on the screen
            if args.display:
                each_image.show()
            # if the -w option was specified then write it to disk
            if args.directory:
                try:
                    each_image.save(args.directory + "/imagenum" + str(imagenumber) + ".jpg")
                    imagenumber += 1
                except Exception as e:
                    print "Unable to write file. " + str(e)
            if args.maps:
                lon, lat = coordinates(each_image)
                if lon and lat:
                    print "http://maps.google.com/maps?q=%.9f,%.9f&z=15" % (lat, lon)
            if args.exif:
                print print_exif(each_image)
        except:
            pass