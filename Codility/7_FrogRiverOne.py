"""
Task: Frog River One
- Find the earliest time when a frog can jump to the other side of a river.
"""

# Time complexity: O(N)
def solution(X, A):
    positions = set()
    for i, pos in enumerate(A):
        if pos <= X:
            positions.add(pos)
        if len(positions) == X:
            return i
    return -1