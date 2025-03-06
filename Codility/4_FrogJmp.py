"""
Task: Frog Jmp
- Count minimal number of jumps from position X to Y.
"""

import math

# Time complexity: O(1)
def solution(X, Y, D):
    return math.ceil((Y-X)/D)