"""
netresec.com
Forensic Challenge 14

Example Bash Script to Process a Given Folder of PCAP Files Through tcpdump
folder=`date +%Y%m%d-%H%M-%Z_description`
filter='host 192.168.1.1'
mkdir ~/$folder
for i in `find /nsm/sensor_data/*-eth*/dailylogs/*/ -type f`; tcpdump -nr $i -w ~/$folder/`echo $i | awk -F/ '{print $NF}'`.pcap $filter; done
mergecap -w ~/$folder/`hostname`_$folder.pcap ~/$folder/snort.log.*
find ~/$folder -type f -size 24c -print0 | xargs -0 rm
"""

from datetime import *

today = date.today()
now = datetime.now()
date = now.strftime("%H:%M:%S")
folder = "{0}{1:02}{2}_{3}".format(today.year, today.month, today.day, date)
filter = "host 192.168.1.1"
mkdir folder