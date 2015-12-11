#!/usr/bin/env python
import struct
import sys,os
import socket
import binascii

#create socket
rawSocket=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))
#ifconfig eth0 promisc up
receivedPacket=rawSocket.recv(2048)
