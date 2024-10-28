def complement_char(c):
    #dictionary to hold complement of each base in sequence
    base_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    if c in base_dict:
        return base_dict[c] #returns complementary value of the base(key)
    else:
        return f"Error: {c} is an Invalid base"
        #return ""


def complement_string(s):
    complement_sequence =  []
    for base in s: #loops over inputted seqequence
        complement_sequence.append(complement_char(base)) #appends compliment of each base to new string 
    return ''.join(complement_sequence) #''.join concatenates all list elements for memory efficiency instead of +=


def longestGap(sequence_length, indexes):
    if len(indexes) <= 1:
        return 0
    else:
        max_gap = 0
        for num in range(len(indexes) - 1): #loop through indexes up to second-to-last number 
            # Calculates gap between current index (num+1 ) and next index (num)
            # Subtracts sequence_length to exclude the sequence itself from the gap calculation
            gap = indexes[num+1] - indexes[num] - sequence_length
            if gap > max_gap: #updates max gap is current gap is larger
                max_gap = gap
        return max_gap


def binding(s, t):
    t_complement =  complement_string(t) #identify complement of short sequence
    binding_sites = []
    for num in range(len(s) - len(t)): # loops through range of long sequence - short string
    # syntax for slice is (start:end)
        if s[num:num+len(t)] == t: # checks if current position matches short sequence
            binding_sites.append(num)   # adds match to string
    return binding_sites

    if len(binding_sites) == 0:
        return -1 #returns -1 if no binding sites were found
    elif len(binding_sites) == 1:
        return binding_sites[0] #returns the only binding site if there is only one
    else:
        return longestGap(len(t), binding_sites) # finds longest gap between binding sites
