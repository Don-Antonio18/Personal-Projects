# PART 1
def makePacket(srcIP, dstIP, length, prt, sp,dp,sqn, pld):
    return ("PK", srcIP, dstIP, [length, prt, [sp,dp], sqn, pld] )

def getPacketSrc(pkt):
    return pkt[1]

def getPacketDst(pkt):
    return pkt[2] # returns 3rd index of tuple

def getPacketDetails(pkt):
    return pkt[3] # returns lst with packet details

def isPacket(pkt):
    #    makes sure input has meets all conditions of packet adt
    return isinstance(pkt, tuple) and pkt[0] == "PK" and isinstance(pkt[1], str) and isinstance(pkt[2], str) \
            and isinstance(pkt[3], list) and len(pkt[3]) == 5 and len(pkt) == 4 
    
def isEmptyPkt(pkt):
    return pkt == ()

#PART 2


    