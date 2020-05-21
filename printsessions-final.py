from scapy.all import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('pcap_file', 
                    help='Packet Capture File to extract sessions from ')
parser.add_argument('-f','--follow_streams',action='store_true',required=False,help='Follow TCP Streams before printing.')
parser.add_argument('-s','--sort',action='store_true',required=False,help='Sort the data before printing it')

args = parser.parse_args()
unsortedpackets = rdpcap(args.pcap_file)
if not args.follow_streams:   #Do this when -f was NOT passed as an option
    packets = unsortedpackets
    for each_packet in packets:
        payload =  "".join([x[Raw].load for x in packets if x.haslayer(Raw)])
        print payload
else:          #Do this when -f WAS passed
    for each_session in unsortedpackets.sessions().values():
        packets = each_session
        if args.sort:    #sort it if -s was passed
            packets = sorted(packets, key=lambda x: x.seq)
        payload =  "".join([x[Raw].load for x in packets if x.haslayer(Raw)])
        print payload

