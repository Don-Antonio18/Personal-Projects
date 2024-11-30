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


#Part 1
def makePacket(srcIP, dstIP, length, prt, sp, dp, sqn, pld):
    return ("PK", srcIP, dstIP,[length, prt, [sp, dp], sqn, pld])

    

def getPacketSrc(pkt):
    return pkt[1]

def getPacketDst(pkt):
    return pkt[2]

def getPacketDetails(pkt):
    return pkt[3]

def isPacket(pkt):
    return (
        isinstance(pkt, tuple) and 
        len(pkt) == 4 and
        pkt[0] == "PK" and 
        isinstance(pkt[1], str) and 
        isinstance(pkt[2], str) and 
        isinstance(pkt[3], list) and 
        len(pkt[3]) == 5
    )
    
def isEmptyPkt(pkt):
    return isPacket(pkt) and pkt == ()

#PART 2: Creating Selector Functions

def getLength(pkt):
    return pkt[3][0]

def getProtocol(pkt):
    return pkt[3][1]

def getSrcPort(pkt):
    return pkt[3][2][0]

def getDstPort(pkt):
    return pkt[3][2][1]

def getSqn(pkt):
    return pkt[3][3]

def getPayloadSize(pkt):
    return pkt[3][4]

# Part 3 : Create Function to Analyse packet
def flowAverage(packet_List
):
    if not packet_List:
        return []  

    total_payload = sum(getPayloadSize(pkt) for pkt in packet_List
    if isPacket(pkt))
    average_payload = total_payload / len(packet_List
    )
    return [pkt for pkt in packet_List
    if getPayloadSize(pkt) > average_payload]

def suspPort(pkt):
    return getSrcPort(pkt) > 500 or getDstPort(pkt) > 500

def suspProto(pkt):
    protocol = getProtocol(pkt)
    ProtocolList = ["HTTP","SMTP","UDP","TCP","DHCP"]
    return protocol not in ProtocolList

def ipBlacklist(pkt):
    src_ip = getPacketSrc(pkt)

    IpBlackList = ["213.217.236.184","149.88.83.47","223.70.250.146","169.51.6.136","229.223.169.245"]
    return src_ip in IpBlackList


#Part 4: Score Packet Abstract Data Type

def calScore(pkt):
    pktscore = 0
    
    # Check if the packet is in the flow average list
    if pkt in flowAverage(packet_List):
        pktscore += 3.56
    
    if suspPort(pkt):
        pktscore += 1.45 #Check for suspicious port
    
    if suspProto(pkt):  
        pktscore += 2.74 #Check for suspitious protocol
    
    if ipBlacklist(pkt):   
        pktscore += 10

    return pktscore


def makeScore(packet_List):
    scorelist = ["SCORE", [(pkt, calScore(pkt)) for pkt in packet_List
    if isPacket(pkt)]]
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

#Part 5: Create Packet Queue

def makePacketQueue():
    return ("PQ" , [])

def contentsQ(q):
    return q[1]

def frontPacketQ(q):
    return q[0]

def addToPacketQ(pkt,q):
    if calScore(pkt) > 5.00:
        pass
    
    q_contents = contentsQ(q)
    position = get_pos(pkt,q_contents)
    q_contents.insert(position, pkt)

    return q

def get_pos(pkt,lst):
    if (lst == []):
        return 0
    elif getSqn(pkt) < getSqn(lst[0]):
        return 0 + get_pos(pkt,[])
    else:
        return 1 + get_pos(pkt,lst[1:])
            
def removeFromPacketQ(q):
    
    contentsQ(q).pop(0)

def isPacketQ(q):
    return isinstance(q, tuple) and len(q) == 2 and q[0] == "PQ" and isinstance(q[1], list)
    

def isEmptPacketQ(q):
    return isPacketQ(q) and contentsQ(q) == []


# Part 6: Stack ADT

def makePacketStack():
    return ("PS" , [])

def contentsStack(stk):
    return stk[1]

def topProjectStack (stk):
    if isPKstack(stk) == False :
        raise ValueError("Argument is not a valid stack.")
    elif isEmptyPKStack(stk):
        raise ValueError("Cannot view the top of an empty stack.")
    else:
        return contentsStack(stk)[-1]  # returns top of stack


def pushProjectStack(pkt,stk):
    if isPacket(pkt):
        contentsStack(stk).append(pkt)
    
    
def popPickupStack(stk):
    if not isPKstack(stk) or isEmptyPKStack(stk):
        raise ValueError("Cannot pop from an invalid or empty stack.")
    contentsStack(stk).pop()

def isPKstack(stk):
    if type(stk) == tuple and len(stk) == 2 and stk[0] == "PS" and isinstance(stk[1], list):
        return True
    else:
        return False

def isEmptyPKStack(stk):
    if not isPKstack(stk): 
        return False
    return contentsStack(stk) == []
    
# Part 7: Sort packet ADT

def sortPackets(scoreList,stack,queue):
    
    [addToPacketQ(packet, queue) for packet in getRegulPkts(scoreList) if isPacket(packet)]
    
    [pushProjectStack(packet, stack) for packet in getSuspPkts(scoreList) if isPacket(packet)]
    
# PArt 8: Main Driver Function 

'''
1. Accepts a list of packets
Format: [(SRC, DST, LEN, PRT, SP, DP, SQN, PLD), (SRC, DST, LEN,
PRT, SP, DP, SQN, PLD)...]

2. created a packet based on packet ADT

3. analyses each packet in list using funcs from part 3

4. Gets suspicion score for each packet

5. add each packet to a score ADT

6. separates packets into packet queue and packet stack based on part 5 & 6

7. Returns the packet queue in order of highest to lowest sequence number

'''

def analysePackets(packet_List):
    
    """ create packet based on packet ADT """
    pkt_ADTs = [makePacket(pkt) for pkt in packet_List
    if isPacket(pkt)]
    

    """ get suspicion score for each packet"""
    sus_List = [calScore(pkt) for pkt in pkt_ADTs]
    
    """ Add each packet to a score ADT"""
    scoreList = [makeScore(pkt) for pkt in pkt_ADTs]
    
    """ separate packets into packet queue and packet stack """
    queue = makePacketQueue()
    stack = makePacketStack()

    sortPackets(scoreList,stack, queue)
    
    """ return packet queue in order of highest to lowest sequence num"""
    sorted_queue = []
    for pkt in queue:
        pos = get_pos(pkt, sorted_queue)
        sorted_queue.insert(pos,pkt)
        
    return ('PQ', [(pkt.srcIP, pkt.dstIP, [pkt.length, pkt.prt, [pkt.sp, pkt.dp], pkt.sqn, pkt.pld]) for pkt in sorted_queue])
    
    
    
    
first_multiple_input = input().rstrip().split()
srcIP = str(first_multiple_input[0])
dstIP = str(first_multiple_input[1])
length = int(first_multiple_input[2])
prt = str(first_multiple_input[3])
sp = int(first_multiple_input[4])
dp = int(first_multiple_input[5])
sqn = int(first_multiple_input[6])
pld = int(first_multiple_input[7])    
    
ProtocolList = ["HTTPS","SMTP","UDP","TCP","DHCP","IRC"]
IpBlackList = ["213.217.236.184","149.88.83.47","223.70.250.146","169.51.6.136","229.223.169.245"]

packet_List = [(srcIP, dstIP, length, prt, sp, dp, sqn, pld),\
("111.202.230.44","62.82.29.190",31,"HTTP",80,20,1562436,38),\
("222.57.155.164","50.168.160.19",22,"UDP",90,5431,1662435,82),\
("333.230.18.207","213.217.236.184",56,"IRC",501,5643,1762434,318),\
("444.221.232.94","50.168.160.19",1003,"TCP",4657,4875,1962433,428),\
("555.221.232.94","50.168.160.19",236,"TCP",7753,5724,2062432,48)]

    
    

    