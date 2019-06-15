#!/usr/bin/env python
# coding: utf8

import socket
from struct import pack
from uuid import getnode as get_mac

dest_ip = [192, 168, 178, 1]  # [127, 0, 0, 1]
local_mac = [int(("%x" % get_mac())[i:i+2], 16) for i in range(0, 12, 2)] # 216, 252, 147, 237, 223, 40
local_ip = [192, 168, 178, 22]

dest_mac = [204, 206, 30, 205, 91, 123] # keine ahnung wem die gehoert todo muesse über ARP protokoll erkundet werden
# d8 fc 93 ed df 26

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
s.bind(("wlp2s0", 0))  # wlp2s0, eth0

MAC_Frame = [
        pack('!6B', *dest_mac),
        pack('!6B', *local_mac),
        #pack('!H', 0x0806), # ARP :: Type of the upcomming packet
        pack('!H', 0x0800), # UDP
        #pack('!H', 0x0XXX), # TCP
        #pack('!H', 0x0XXX), # ICMP
]

# 8 bit = b'11111111 = 1Byte 0 0xFF
# 0xFFFF = 2 Byte = 16 bit
# 0xFF 0xFF 0xFF = 3 Byte = 24 bit
# 0xFF 0xFF 0xFF 0xFF = 4 Bytr = 32 bit

IP_Frame = [	
        pack('!B', 0x45), # version and HIL   8 bit 1B !B
        pack('!B', 0x00), # TOS	            8 bit 1B !B
        pack('!H', 0x0029), # Total Length  16bit 2B !H
        pack('!H', 0xfc10), # Identification     16bit 2B !H
        pack('!H', 0x4000), # Flags and Fragment Offset   16bit 2B !H
        pack('!B', 0x40), # TTL     8 bit 1B !B
        pack('!B', 0x11), # Protocol (UDP = 17= 0x11)  8 bit 1B !B
        pack('!H', 0x7d8c), # Header checksum           16bit 2B !H
        pack('!4B', *local_ip), # source Address        32bit 4B !4B
        pack('!4B', *dest_ip), # Destination Address     32bit 4B !4B
        # pack('!H', 0x0001), # Options and Padding
    ]

UDP_Frame = [	
        pack('!H', 0xaec4), # source port 44740
        pack('!H', 0x138d), # Destination port 5005
        pack('!H', 0x0015), # Length 343
        pack('!H', 0x16bd), # Checksum
    ]

Payload = [	
        pack('!13B', 0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x20, 0x57, 0x6f, 0x72, 0x6c, 0x64, 0x21), # HRD  48656c6c6f2c20576f726c6421
    ]

print(MAC_Frame+IP_Frame+UDP_Frame+Payload)

s.send(b''.join(MAC_Frame+IP_Frame+UDP_Frame+Payload))
