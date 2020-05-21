#Copyright 2015 Mark Baggett - Driftnet scapy
#for exclusive use with Mark Baggett's Python Course

from scapy.all import * 
from cStringIO import StringIO
from PIL import Image
from PIL.ExifTags import TAGS

def coordinates(ImageObject):
    """This function takes in a PIL Image Object and returns a longitude and latitude. For example: xlong,xlat = coordinates(imageobject) """
    info = ImageObject._getexif()
    if not info:
        return 0,0
    # 34853: contains 'GPSInfo'
    # info[34853][1] = 'N'
    # Latitude at info[34853][2] =  ((49, 1), (4363, 1000), (0, 1))
    # info[34853][3] = 'W'
    # Longitude at info[34853][4] =  ((123, 1), (2103, 1000), (0, 1))
    latDegrees = info[34853][2][0][0]/float(info[34853][2][0][1]) 
    latMinutes = info[34853][2][1][0]/float(info[34853][2][1][1])/60 
    latSeconds = info[34853][2][2][0]/float(info[34853][2][2][1])/3600 
    lonDegrees = info[34853][4][0][0]/float(info[34853][4][0][1]) 
    lonMinutes = info[34853][4][1][0]/float(info[34853][4][1][1])/60 
    lonSeconds = info[34853][4][2][0]/float(info[34853][4][2][1])/3600 
    # correct the lat/lon based on N/E/W/S 
    latitude = latDegrees + latMinutes + latSeconds
    if info[34853][1] == 'S':
        latitude*= -1
    longitude = lonDegrees + lonMinutes + lonSeconds 
    if info[34853][3] == 'W':
        longitude*=-1
    return longitude,latitude


def eliminate_duplicates(packets):
    """The eliminate_duplicates function will accept a scapy PacketList as its one and only argument.  It will eliminate any packets that have the same sequence number accepting the last packet to arrive.  It will return a list of unique packets."""
    keys = {}
    for packet in packets:
        index=packet[TCP].seq
        keys[index]=packet
    return keys.values()

def verify_checksum(packet):
    """The verify_checksum function will look at the checksum of a single packet.  It will return True if the checksum is valid and False if the checksum is not valid for that packet."""
    #http://stackoverflow.com/questions/6665844/comparing-tcp-checksums-with-scapy
    oldChecksum=packet[TCP].chksum
    del packet[TCP].chksum
    packet=IP(str(packet[IP]))
    newChecksum=packet[TCP].chksum
    return oldChecksum==newChecksum

def print_exif(imageobject):
    """The print_exif function will take in a PIL ImageObject and print all of the EXIF data along with the associated EXIF Tag"""
    exifdict=imageobject._getexif()
    if exifdict:
       for name,data in exifdict.items():
           tagname="unknown-tag"
           if name in TAGS:
               tagname=TAGS[name]
           print "TAG:%s (%s) is assigned %s" % (name,tagname,data) 
    return

def payload_as_string(astream):
    """The payload_as_string function will take in a scapy PacketList.  It will then extract all of the bytes of data in the payload of those packets and return them as a single string. Feed this function the results of follow_stream. """
    rawstring=""
    for a in sorted(astream, key=lambda x:x.seq):
        rawstring+=a[Raw].load
    return rawstring

def read_filtered_packets(pathtofile):
    """This function reads the specified pcap file.  It wil calls verify_checksum and eliminate_duplicates and then returns only those TCP packets that have a packet payload"""
    temppac0=rdpcap(pathtofile)
    temppac1=[a for a in temppac0 if a.haslayer("TCP") and a.haslayer("Raw")]
    temppac2=eliminate_duplicates([a for a in temppac1 if verify_checksum(a)])
    return scapy.plist.PacketList(temppac2)

def http_stream_to_images(packet_stream):
    """This function takes in a packet list containing an HTTP stream where JPG images are downloaded.  It returns a list of PIL image objects for any jpegs that exist in the stream"""
    packet_stream = sorted(packet_stream, key = lambda x:x[TCP].seq)
    list_of_images = []
    jpgstart="\xff\xd8"
    jpgend="\xff\xd9"
    raw_string = "".join([x[Raw].load for x in packet_stream if x.haslayer(Raw)])
    for each_response in raw_string.split("HTTP/1")[1:]:
        jpg=re.search(r'\xff\xd8.*\xff\xd9',each_response,re.DOTALL)
        if jpg:
            try:
                list_of_images.append(Image.open(StringIO(jpg.group())))
            except:
                print "Invalid Image error "
    return list_of_images
        
def checkseq(unsortedpackets):
    """This function takes in a list of unsorted packet.  It will print a message if it finds any duplicate sequence numbers, or missing sequence numbers."""
    #this function (which isn't used) checks for missing or duplicate packets
    packets=sorted(unsortedpackets, key=lambda x:x.seq)
    curseq=packets[0]["TCP"].seq
    nextseq=int(packets[0]["TCP"].seq) + len(packets[0]["Raw"].load)
    for a in packets[1:]:
        if a["TCP"].seq==nextseq:
            curseq=a["TCP"].seq
            nextseq=int(a["TCP"].seq) + len(a["Raw"].load)
            continue
        if a["TCP"].seq==curseq:
            print "Duplicate Sequence Number "+str(curseq)
            continue
        if a["TCP"].seq<nextseq:
            print "Packet Missing after "+str( a["TCP"].seq )

class img_list(list):
    def read_pcap(self, pcap):
        all_packets = read_filtered_packets("icanstalku.pcap")
        for eachp in all_packets.sessions().values():
            stream_images = http_stream_to_images(eachp)
            if len(stream_images) == 0:
                continue
            self.extend(stream_images)

    def google_maps():
        for item in self:
            lon,lat = coordinate(item)
            if lon or lat:
                print "http://maps.google.com/maps?q=%.9f,%.9f&z=15" % (lat, lon)

def main():
    all_packets = read_filtered_packets("icanstalku.pcap")
    for each_stream in all_packets.sessions().values():
        stream_images = http_stream_to_images(each_stream)
        if len(stream_images) == 0:
            continue
        for each_image in stream_images:
            try:
                each_image.show()
                print print_exif(each_image)
                print coordinates(each_image)
            except:
                pass

if __name__=="__main__":
    main()

