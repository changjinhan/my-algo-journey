"""
Task: Binary Gap 
- Find the longest sequence of zeros in a binary representation
"""

def solution(N):
    bin_num = bin(N)[2:]
    max_binary_gap = 0
    cur_binary_gap = 0
    counting = False

    for bit in bin_num:
        if bit == '1':
            if counting:
                max_binary_gap = max(max_binary_gap, cur_binary_gap)
            counting = True
            cur_binary_gap = 0
        elif counting:
            cur_binary_gap += 1

    return max_binary_gap