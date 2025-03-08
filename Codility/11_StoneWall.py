"""
Task: Stone Wall
- Cover "Manhattan skyline" using the minimum number of rectangles.
"""

def solution(H):
    stack = []
    blocks = 0

    for height in H:
        while stack and stack[-1] > height:
            stack.pop()

        if stack and stack[-1] == height:
            continue

        stack.append(height)
        blocks += 1

    return blocks


