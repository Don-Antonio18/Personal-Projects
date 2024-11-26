""" 
Group information:
Antonio Kerr: 620170333
Danecia Watt: 
"""
import math
import os
import random
import re
import sys
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
        Note: length of packet ADT not equal to length of packet """
    return pkt[3][0]

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


#   PART 3: Create Function to Analyse packet

def flowAverage(pkt_list):

    if not pkt_list:
        return []  
    
    total_payload = sum(getPayloadSize(pkt) for pkt in pkt_list if isPacket(pkt))
    average_payload = total_payload / len(pkt_list)
    return [pkt for pkt in pkt_list if isPacket(pkt) and getPayloadSize(pkt) > average_payload]
    
    
def suspPort(pkt):

    return getSrcPort(pkt) > 500 or getDstPort(pkt) > 500

def suspProto(pkt):

    protocol = getProtocol(pkt)
    ProtocolList = ["HTTP","SMTP","UDP","TCP","DHCP"]
    return protocol not in ProtocolList


def ipBlacklist(pkt):

    src_ip = getPacketSrc(pkt)
    IpBlackList = ["213.217.236.184","444.221.232.94","149.88.83.47","223.70.250.146","169.51.6.136","229.223.169.245"]
    return src_ip in IpBlackList


# Part 4: Score Packet ADT

ProtocolList = ["HTTP","SMTP","UDP","TCP","DHCP"]
IpBlackList = ["213.217.236.184","444.221.232.94","149.88.83.47","223.70.250.146","169.51.6.136","229.223.169.245"]


def calScore(pkt):
    pktscore = 0
    # Check if the packet is in the flow average list
    if pkt in flowAverage(pkt_list): #type: ignore
        pktscore += 3.56
    
    if suspPort(pkt):
        pktscore += 1.45 #Check for suspicious port
    
    if suspProto(pkt):  
        pktscore += 2.74 #Check for suspitious protocol
    
    if ipBlacklist(pkt):   
        pktscore += 10

    return pktscore



    

def makeScore(pkt_list):
    scorelist = ["SCORE", [(pkt, calScore(pkt)) for pkt in pkt_list if isPacket(pkt)]]
    return scorelist

def addPacket(scorelist, pkt):
    scorelist[1].append((pkt, calScore(pkt)))

def getSuspPkts(scorelist):
    if not isScore(scorelist):
        return []  # Return an empty list if the scorelist is invalid
    return [pkt for pkt, score in scorelist[1] if calScore(pkt) > 5.00 ]
    
def getRegulPkts(scorelist):
    if not isScore(scorelist):
        return []  # Return an empty list if the scorelist is invalid
    
    return [pkt for pkt, score in scorelist[1] if 0 <= calScore(pkt) <= 5.00]

def isScore(scorelist):
    return (
        isinstance(scorelist, list)
        and scorelist[0] == "SCORE"
        and isinstance(scorelist[1], list)
        and isinstance(scorelist[1][0], tuple)
    )

def isEmptyScore(scorelist):
    return isScore(scorelist) and scorelist[1] == []


# PART 5: Packet Queue ADT


def makePacketQueue():
    return ("PQ" , []) # (packet, list of packetsw)

def contentsQ(q): # returns list of packets
    return q[1]

def frontPacketQ(q):
    return q[1][0]

def addToPacketQ(pkt,queue):
    contentsQ(queue).append(pkt)

def get_pos(pkt,lst):
    if (lst == []):
        return 0
    elif getSqn(pkt) < getSqn(lst[0]):
        return 0 + get_pos(pkt,[])
    else:
        return 1 + get_pos(pkt,lst[1:])
            
def removeFromPacketQ(queue):
    if contentsQ(queue):
        contentsQ(queue).pop(0)
    else:
        return []

def isPacketQ(queue):
    return isinstance(queue, tuple) and queue[0] == "PQ" and isinstance(queue[0], str) and isinstance(queue[1], list) and len(queue) == 2
    
def isEmptPacketQ(queue):
    return not isPacketQ(queue) or contentsQ(queue) == [] 







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