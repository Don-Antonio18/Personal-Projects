# ID Number: 620170333
# HackerRank Handle: antoniokerruni
# HackerRank Exercise: Ciphertext Challenge

#code submission from HackerRank:

def encrypt(Message):
    if Message == "":
        return ""
    else:
        char = ord(Message[0]) 
        if char % 2 != 0:  
            char += 4       
        else:               
            char -= 4       
        return chr(char) + encrypt(Message[1:])

  
def decrypt(cypher):
    if cypher == "":
        return ""
    else:
        char = ord(cypher[0]) 
        if char % 2 == 0:  
            char += 4       
        else:               
            char -= 4       
        return chr(char) + decrypt(cypher[1:])
