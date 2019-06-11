import socket
from struct import pack
from uuid import getnode as get_mac

# UDP_IP = "127.0.0.1"
# UDP_PORT = 5005
# MESSAGE = "Hello, World!"

dest_ip = [192, 168, 178, 1]  # [10, 7, 31, 99] [127, 0, 0, 1]
local_mac = [int(("%x" % get_mac())[i:i+2], 16) for i in range(0, 12, 2)] # 216, 252, 147, 237, 223, 40
local_ip = [int(x) for x in socket.gethostbyname(socket.gethostname()).split('.')]
local_ip = [192, 168, 178, 22]

#print ("local_mac", local_mac)
#print ("local ip", local_ip)
#print ("destination ip ", dest_ip)

# cc ce 1e cd 5b 7b router mac [204, 206, 193, 205, 91, 123]
#print (hex(216))
#print (int("ccce1ecd5b7b", 16))
# print(int("cc", 16))
# print(int("ce", 16))
# print(int("1e", 16))
# print(int("cd", 16))
# print(int("5b", 16))
# print(int("7b", 16))
# print (int("d8fc93eddf28", 16))
# d8 fc 93 ed df 28 eigene mac
dest_mac = [204, 206, 30, 205, 91, 123]


s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(("wlp2s0", 0))  # wlp2s0 eth0

MAC_FRAME = [
        pack('!6B', *dest_mac),
        pack('!6B', *local_mac),
        pack('!H', 0x0806), # Type of the upcomming packet
]


ARP_FRAME = [	
        pack('!H', 0x0001), # HRD
        pack('!H', 0x0800), # PRO
        pack('!B', 0x06), # HLN
        pack('!B', 0x04), # PLN 
        pack('!H', 0x0001), # OP
        pack('!6B', *local_mac), # SHA
        pack('!4B', *local_ip), # SPA
        pack('!6B', *(0x00,)*6), # THA
        pack('!4B', *dest_ip), # TPA
    ]


IP_Frame = [	
        pack('!H', 0x0001), # HRD
    ]

UDP_Frame = [	
        pack('!H', 0x0001), # HRD
    ]

print(MAC_FRAME+ARP_FRAME)

s.send(b''.join(MAC_FRAME+ARP_FRAME))
