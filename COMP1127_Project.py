import math
import os
import random
import re
import sys
""" 
Group information:
Antonio Kerr: 620170333
Danecia Watt: 
"""


#PART 1; creating packet ADT
def makePacket(srcIP, dstIP, length, prt, sp,dp,sqn, pld):
    return ("PK", srcIP, dstIP, [length, prt, [sp,dp], sqn, pld] )

def getPacketSrc(pkt):
    """ returns srcIP frm tuple """
    return pkt[1] 

def getPacketDst(pkt):
    """returns dstIP frm tuple"""
    return pkt[2] 

def getPacketDetails(pkt):
    """returns lst with packet details"""
    return pkt[3] 

def isPacket(pkt):
    """makes sure input has meets all conditions of packet adt
        isinstance() takes in (variable, datatype(s)_to_validate) and returns True/False """
    return isinstance(pkt, tuple) and pkt[0] == "PK"  and len(pkt) == 4 \
    and isinstance(pkt[1], str)         \
    and isinstance(pkt[2], str)         \
    and isinstance(pkt[3], list)        \
    and len(pkt[1]) > 0                 \
    and len(pkt[2]) > 0                 \
    and len(pkt[3]) == 5                \
    and isinstance(pkt[3][0], int)      \
    and isinstance(pkt[3][1], str)      \
    and pkt[3][1] != ""                 \
    and isinstance(pkt[3][2], list)     \
    and len(pkt[3][2]) == 2             \
    and pkt[3][2] != []                 \
    and isinstance(pkt[3][2][0], int)   \
    and isinstance(pkt[3][2][1], int)   \
    and isinstance(pkt[3][3], int)      \
    and pkt[3][3] >= 0                  \
    and isinstance(pkt[3][4], int)      \
    and pkt[3][4] >= 0           
    
    
    
def isEmptyPkt(pkt):
    """returns True if pkt is tuple data type & false otherwise"""
    return pkt == () 

#PART 2: Creating Selector Functions

def getLength(pkt):
    """ returns length of packet (everything except tuple tag)
        Note: length of packet ADT ≠ length of packet """
    return len(pkt[3][0])

def getProtocol(pkt):
    """ returns protocol of packet"""
    return pkt[3][1]

def getSrcPort(pkt):
    """returns source port of packet"""
    return pkt[3][2][0]

def getDstPort(pkt):
    """ returns destination port of packet"""
    return pkt[3][2][1]

def getSqn(pkt):
    """ returns sequence number of packet"""
    return pkt[3][3]

def getPayloadSize(pkt):
    """ returns payload size of packet"""
    return pkt[3][4]


#! DEBUGGING

pkt = makePacket('111.202.230.44', '62.82.29.190', 3, 'HTTP', 80, 3463, 1562431, 8)
print("DEBUG: Packet Created:", pkt)
print()

print("DEBUG: Validation Results:")
print("Is Tuple:", isinstance(pkt, tuple))
print("Starts with 'PK':", pkt[0] == "PK")
print("Source IP is String:", isinstance(pkt[1], str))
print("Destination IP is String:", isinstance(pkt[2], str))
print("Details are List:", isinstance(pkt[3], list))
print("Details Length is 5:", len(pkt[3]) == 5)
print("Packet Length is 4:", len(pkt) == 4)
print()

print("DEBUG: Protocol =>", getProtocol(pkt))
print("DEBUG: Source Port =>", getSrcPort(pkt))
print("DEBUG: Destination Port =>", getDstPort(pkt))
print("DEBUG: Sequence Number =>", getSqn(pkt))
print("DEBUG: Payload Size =>", getPayloadSize(pkt))
print()

