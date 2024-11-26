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
    # Write your code here
    if not pkt_list:
        return []  
    
    total_payload = sum(getPayloadSize(pkt) for pkt in pkt_list if isPacket(pkt))
    average_payload = total_payload / len(pkt_list)
    return [pkt for pkt in pkt_list if getPayloadSize(pkt) > average_payload]
    
    
def suspPort(pkt):
    # Write your code here
    return getSrcPort(pkt) > 500 or getDstPort(pkt) > 500

def suspProto(pkt):
    # Write your code here
    protocol = getProtocol(pkt)
    ProtocolList = ["HTTP","SMTP","UDP","TCP","DHCP"]
    return protocol not in ProtocolList


def ipBlacklist(pkt):
    # Write your code here
    src_ip = getPacketSrc(pkt)
    IpBlackList = ["213.217.236.184","444.221.232.94","149.88.83.47","223.70.250.146","169.51.6.136","229.223.169.245"]
    return src_ip in IpBlackList


# Part 4: Score Packet ADT

def calScore(pkt):
    pktscore = 0
    
    # Check if the packet is in the flow average list
    if pkt in flowAverage(pkt_list):
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



pk1 = makePacket("111.202.230.44","62.82.29.190",31,"HTTP",80,20,1562431,38)
pk2 = makePacket("222.57.155.164","50.168.160.19",22,"UDP",90,5431,1662431,82)
pk3 = makePacket("333.230.18.207","213.217.236.184",56,"IRC",501,5643,1762431,318)
pk4 = makePacket("444.221.232.94","50.168.160.19",1003,"TCP",4657,4875,1962431,428)
pk5 = makePacket("555.221.232.94","50.168.160.19",236,"TCP",7753,5724,2062431,48)

pkt_list = [pkt,pk1,pk2,pk3,pk4]

ProtocolList = ["HTTP","SMTP","UDP","TCP","DHCP"]
IpBlackList = ["213.217.236.184","444.221.232.94","149.88.83.47","223.70.250.146","169.51.6.136","229.223.169.245"]

ScoreList = makeScore(pkt_list)
addPacket(ScoreList, pk5)
    






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