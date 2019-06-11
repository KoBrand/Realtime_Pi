import socket
from struct import pack
from uuid import getnode as get_mac

dest_ip = [192, 168, 178, 1]  # [127, 0, 0, 1]
local_mac = [int(("%x" % get_mac())[i:i+2], 16) for i in range(0, 12, 2)] # 216, 252, 147, 237, 223, 40
local_ip = [192, 168, 178, 22]

dest_mac = [204, 206, 30, 205, 91, 123] # keine ahnung wem die gehört -> todo müsse über ARP protokoll erkundet werden


s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
s.bind(("wlp2s0", 0))  # wlp2s0, eth0

MAC_FRAME = [
        pack('!6B', *dest_mac),
        pack('!6B', *local_mac),
        #pack('!H', 0x0806), # ARP :: Type of the upcomming packet
        pack('!H', 0x0800), # UDP
        #pack('!H', 0x0XXX), # TCP
        #pack('!H', 0x0XXX), # ICMP
]

IP_Frame = [	
        pack('!H', 0x0001), # version
        pack('!H', 0x0001), # HIL
        pack('!H', 0x0001), # TOS
        pack('!H', 0x0001), # Total Length
        pack('!H', 0x0001), # Identification
        pack('!H', 0x0001), # Flags
        pack('!H', 0x0001), # Fragment Offset
        pack('!H', 0x0001), # TTL
        pack('!H', 0x0001), # Protocol
        pack('!H', 0x0001), # Header checksum
        pack('!H', 0x0001), # source Address
        pack('!H', 0x0001), # Destination Address
        # pack('!H', 0x0001), # Options and Padding
    ]

UDP_Frame = [	
        pack('!H', 0x0001), # HRD
    ]

print(MAC_FRAME+IP_FRAME)

s.send(b''.join(MAC_FRAME+ARP_FRAME))
