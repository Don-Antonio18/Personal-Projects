# PART 1
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
    """makes sure input has meets all conditions of packet adt"""
    return isinstance(pkt, tuple) \
    and pkt[0] == "PK" \
    and isinstance(pkt[1], str) \
    and isinstance(pkt[2], str) \
    and isinstance(pkt[3], list) \
    and len(pkt[3]) == 5 \
    and len(pkt) == 4 
    
def isEmptyPkt(pkt):
    """returns True if pkt is tuple data type & false otherwise"""
    return pkt == () 

#PART 2

