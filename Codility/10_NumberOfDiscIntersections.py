"""
Task: Number of Disc Intersections
- Compute the number of intersections in a sequence of discs.
"""

def solution(A):
    N = len(A)
    start_points = sorted([i-A[i] for i in range(N)])
    end_points = sorted([i+A[i] for i in range(N)])
    j = 0
    open_discs = 0
    intersections = 0
    for i in range(N):
        while j < N and start_points[j] <= end_points[i]:
            open_discs += 1
            j += 1
        open_discs -= 1
        intersections += open_discs

        if intersections > 10_000_000:
            return -1

    return intersections
    