"""
Task: Cyclic Rotation
- Rotate an array to the right by a given number of steps.
"""

def solution(A, K):
    # Initialize new_A to store the rotated result
    length = len(A)
    new_A = [0] * length

    # Shift each element to its new position after K rotations
    for idx in range(length):
        new_A[(idx + K)%length] = A[idx]

    return new_A