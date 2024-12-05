def excludePunNum(input_string):
    puncs = ",.-?!;:^"
    new_lst = ""
    for char in input_string:
        if char in puncs or char.isdigit():
            continue
        new_lst += char
    return new_lst

def encoded_string(lst):
    if lst == "":
        return ""
    else:
        char = ord(lst[0])
        if char % 2 == 0:
            char += 4
        else:
            char += 2
        return chr(char) + encoded_string(lst[1:])

def decoded_string(lst):
    if lst == "":
        return ""
    else:
        char = ord(lst[0])
        if char % 2 == 0:
            char -= 4
        else:
            char -= 2
        return chr(char) + decoded_string(lst[1:])

def stringList(str1):
    return str1.split()

def encodedList(lst):
    if lst == []:
        return []
    else:
        return encodedList(lst[1:]) + [encoded_string(lst[0])]

def decodedList(lst):
    if lst == []:
        return []
    else:
        return decodedList(lst[1:]) + [decoded_string(lst[0])]

def main(s):
    slst = excludePunNum(s)
    eList = encodedList(stringList(slst))
    dList = decodedList(eList)
    print("Given string =>", s)
    print("Punctuation removed =>", slst)
    print("List Encoded =>", eList)
    print("List Decoded =>", dList)
    print("Encoded Message =>", ' '.join(eList))

main("COMP1126!! Sci2024 is a, : lot of, fun?")
