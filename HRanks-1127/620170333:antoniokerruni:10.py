#   ID Number: 620170333
#   Hackerrank Handle: antoniokerruni
#   Hackerank Exercise: DNA Binding

def complement_char(c):
    base_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    if c in base_dict:
        return base_dict[c]
    else:
        return ""

def complement_string(s):
    complement_sequence = []
    for base in s:
        complement_sequence.append(complement_char(base))
    return ''.join(complement_sequence)

def longestGap(ln, lst):
    if len(lst) <= 1:
        return 0
    else:
        max_gap = 0
        for num in range(len(lst) - 1):
            gap = lst[num+1] - lst[num] - ln
            if gap > max_gap:
                max_gap = gap
        return max_gap  

def binding(s, t):
    t_complement = complement_string(t)
    binding_sites = []
    
    for num in range(len(s) - len(t) + 1):
        if s[num:num+len(t)] == t_complement:
            binding_sites.append(num)
    
    if len(binding_sites) == 0:
        return -1
    elif len(binding_sites) == 1:
        return binding_sites[0]
    else:
        return longestGap(len(t), binding_sites)