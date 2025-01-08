def stringList(str1):
    # splits string into list of strings
    return str1.split() 

def encodedList(lst):
    if lst == []:  # Base case: empty list
        return []
    else:
        # encocdes the list and then reverse the order
        return encodedList(lst[1:]) + [encoded_string(lst[0])]
    
def decodedList(lst):
    if list == []:
        return []
    else: 
        # decodes the list reverses the list
        return decodedList(lst[1:]) + [decoded_string(lst[0])]
    

from lab4Q1 import excludePunNum
def main(s):
    slst=excludePunNum(s)
    eList = encodedList(stringList(slst))
    dList = decodedList(eList)
    print("Given string =>", s)
    print("Punctuation removed =>", slst)
    print("List Encoded =>", eList)
    print("List Decoded =>", dList)
    print("Encoded Message =>",' '.join(eList))