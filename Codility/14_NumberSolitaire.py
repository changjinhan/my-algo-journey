"""
Task: Number Solitaire
- In a given array, find the subset of maximal sum in which the distance between consecutive elements is at most 6.
"""

def solution(A):
    N = len(A)
    max_sum = [A[0]] + [float('-inf')] * (N-1)
    for i in range(1, N):
        for j in range(1,7):
            if i-j >= 0:
                max_sum[i] = max(max_sum[i], A[i] + max_sum[i-j])
    return max_sum[-1]