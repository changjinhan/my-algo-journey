"""
Task: Perm Missing Elem
- Find the missing element in a given permutation.
"""

def solution(A):
    N = len(A)
    ideal_sum = sum(list(range(1, N+1)))
    real_sum = sum(A)
    missing_num = N+1 - (real_sum - ideal_sum)
    return missing_num