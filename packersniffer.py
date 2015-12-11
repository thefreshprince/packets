#!/usr/bin/env python
import struct
import sys,os
import socket
import binascii

#create socket
rawSocket=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))
#ifconfig eth0 promisc up
receivedPacket=rawSocket.recv(2048)

#Ethernet Header
ethernetHeader=receivedPacket[0:14]
ethrheader=struct.unpack("!6s6s2s",ethernetHeader)
destinationIP= binascii.hexlify(ethrheader[0])
sourceIP= binascii.hexlify(ethrheader[1])
protocol= binascii.hexlify(ethrheader[2])
