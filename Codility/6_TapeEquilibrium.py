"""
Task: Tape Equilibrium
- Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
"""

def solution(A):
    total = sum(A)
    first_part_sum = 0
    for idx in range(1, len(A)):
        first_part_sum += A[idx-1]
        cur_diff = abs((total - first_part_sum) - first_part_sum)
        if idx == 1:
            min_diff = cur_diff
        else:
            min_diff = min(min_diff, cur_diff)
    return min_diff