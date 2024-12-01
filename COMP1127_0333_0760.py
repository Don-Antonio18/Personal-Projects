""" 
Group information:

Antonio Kerr: 620170333
Danecia Watt: 620170760
"""

import math
import os
import random
import re
import sys

""" Part 1: Create Packet ADT """

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


""" PART 2: Creating Selector Functions for Packet Details of Packet ADT """

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

""" Part 3 : Create Function to Analyse packet """
def flowAverage(pkt_List):
    valid_packets = [pkt for pkt in pkt_List if isPacket(pkt)]
    if not valid_packets:
        return []
    
    """Average = total / number of indexes (a.k.a length)""" 
    total_payload = sum(getPayloadSize(pkt) for pkt in valid_packets)
    average_payload = total_payload / len(valid_packets)
    return [pkt for pkt in valid_packets if getPayloadSize(pkt) > average_payload]


def suspPort(pkt):
    """ Any # greater than 500 is considered suspicious """
    return getSrcPort(pkt) > 500 or getDstPort(pkt) > 500

def suspProto(pkt):
    protocol = getProtocol(pkt)
    ProtocolList = ["HTTP","SMTP","UDP","TCP","DHCP"]
    return protocol not in ProtocolList

def ipBlacklist(pkt):
    src_ip = getPacketSrc(pkt)
    """ Identifies whether or not IP address of packet is blacklisted """
    return src_ip in IpBlackList


""" Part 4: Score Packet Abstract Data Type """

def calScore(pkt):
    """ Initialising packet score variable """
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


def makeScore(pkt_List):
    scorelist = ["SCORE", [(pkt, calScore(pkt)) for pkt in pkt_List if isPacket(pkt)]]
    return scorelist

def addPacket(scorelist, pkt):
    scorelist[1].append((pkt, calScore(pkt)))

def getSuspPkts(scorelist):
    if not isScore(scorelist):
        """ Return an empty list if the scorelist is invalid """
        return []  
    """ otherwise returns list of suspicious packets """
    return [pkt for pkt, score in scorelist[1] if calScore(pkt) > 5.00 ]
    
def getRegulPkts(scorelist):
    if not isScore(scorelist):
        """  Returns an empty list if the scorelist is invalid"""
        return []  
    """ otherwise returns list of regular packets """
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


""" Part 5: Create Packet Queue """

def makePacketQueue():
    return ("PQ" , [])

def contentsQ(q):
    return q[1]

def frontPacketQ(q):
    """ Queue uses FIFO, so first index == front """
    return q[0]

def addToPacketQ(pkt,q):
    if calScore(pkt) > 5.00:
        """ function ignores all suspicious packets """
        pass
    
    q_contents = contentsQ(q)
    position = get_pos(pkt,q_contents)
    """ inserts packet at proper position in queue """
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
    """ removes the first index, which is at the front of the queue """
    contentsQ(q).pop(0)

def isPacketQ(q):
    return isinstance(q, tuple) and len(q) == 2 and q[0] == "PQ" and isinstance(q[1], list)
    

def isEmptPacketQ(q):
    return isPacketQ(q) and contentsQ(q) == []


""" Part 6: Stack ADT """

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
        """ Stack uses LIFO, so last index == top """
        return contentsStack(stk)[-1]  


def pushProjectStack(pkt,stk):
    if isPacket(pkt):
        """ adds elmnt to top of stack """
        contentsStack(stk).append(pkt)
    
    
def popPickupStack(stk):
    """ checks validity of stack """
    if not isPKstack(stk) or isEmptyPKStack(stk):
        raise ValueError("Cannot pop from an invalid or empty stack.")
    """ removes top of stack  """
    contentsStack(stk).pop()

def isPKstack(stk):
    """ validates conditionals of stack """
    if type(stk) == tuple \
    and len(stk) == 2 \
    and stk[0] == "PS" \
    and isinstance(stk[1], list):
        return True
    else:
        return False

def isEmptyPKStack(stk):
    """ check validity of stack"""
    if not isPKstack(stk): 
        return False
    """ Boolean: returns True if stack is an empty list: """
    return contentsStack(stk) == []
    
""" Part 7: Sort packet ADT """

def sortPackets(scoreList,stack,queue):
    """ adds each regular packet to queue if it is a valid packet: """
    [addToPacketQ(packet, queue) for packet in getRegulPkts(scoreList) if isPacket(packet)]
    
    """ adds each suspicious packet to stack if it is a valid packet: """
    [pushProjectStack(packet, stack) for packet in getSuspPkts(scoreList) if isPacket(packet)]


""" Part 8: Main Driver Function """

def analysePackets(packet_List):
    """ declares pkt_List as a global variable, 
    meaning all functions in program can access it."""
    global pkt_list
    
    pkt_list = []
    
    """ loops through each packet in packet list: """
    for pkt in packet_List:
        """ adds unpacked(*) packet tuple to new packet list: """
        pkt_list.append(makePacket(*pkt))
    
    """ makes a scorelist from packet list """
    scoreList = makeScore(pkt_list)
    
    """ create a empty queue and stack """
    Packet_queue = makePacketQueue()
    Packet_stack = makePacketStack()
    
    """ sorts packet list into queue and stack
    based on suspicion score of each packet.
    
    Note: SortPackets already sorts packet queue into descending sqn order."""
    sortPackets(scoreList, Packet_stack, Packet_queue)
    
    return Packet_queue


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

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
    packet_List = [
    (srcIP, dstIP, length, prt, sp, dp, sqn, pld),
    ("111.202.230.44", "62.82.29.190", 31, "HTTP", 80, 20, 1562436, 338),
    ("222.57.155.164", "50.168.160.19", 22, "UDP", 790, 5431, 1662435, 812),
    ("333.230.18.207", "213.217.236.184", 56, "IMCP", 501, 5643, 1762434, 3138),
    ("444.221.232.94", "50.168.160.19", 1003, "TCP", 4657, 4875, 1962433, 428),
    ("555.221.232.94", "50.168.160.19", 236, "HTTP", 7753, 5724, 2062432, 48)
]

    
    fptr.write('Forward Packets => ' + str(analysePackets(packet_List)) + '\n')
    
    fptr.close()