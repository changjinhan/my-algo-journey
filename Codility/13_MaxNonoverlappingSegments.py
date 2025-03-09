"""
Task: Max Nonoverlapping Segments
- Find a maximal set of non-overlapping segments.
"""

# Time complexity: O(N)
def solution(A, B):
    if len(A) == 0:
        return 0

    count = 1
    last_end = B[0]
    for start, end in zip(A[1:], B[1:]):
        if start > last_end:
            count += 1
            last_end = end
        
    return count