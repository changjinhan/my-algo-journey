"""
Task: Passing Cars
- Count the number of passing cars on the road.
"""

def prefix_sum(A):
    N = len(A)
    P = [0] * (N+1)
    for i in range(1, N+1):
        P[i] = P[i-1] + A[i-1]
    return P

def count_total(P, x, y):
    return P[y+1] - P[x]

# Time complexity: O(N)
def solution(A):
    N = len(A)
    num_pairs = 0
    P = prefix_sum(A)
    for i in range(N):
        if A[i] == 0:
            num_pairs += count_total(P, i, N-1)
        if num_pairs > 10**9:
            return -1
    return num_pairs