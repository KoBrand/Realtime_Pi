import socket

UDP_IP = "192.168.178.39"
UDP_PORT = 5555
MESSAGE = "Hello, World!"

# print "UDP target IP:", UDP_IP
# print "UDP target port:", UDP_PORT
# print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet, UDP
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

# to send an MAC paket use
# s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# s.bind(("eth0", 0))
"""
dest_ip = [10, 7, 31, 99]
    local_mac = [int(("%x" % get_mac())[i:i+2], 16) for i in range(0, 12, 2)]
    local_ip = [int(x) for x in socket.gethostbyname(socket.gethostname()).split('.')]


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
    print(ARP_FRAME)
"""
# s.send(b''.join(ARP_FRAME))



