"""
Task: Max Counters
- Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.
"""

# Time complexity: O(N + M)
def solution(N, A):
    result = [0] * N
    max_counter = 0
    last_update = 0
    for num in A:
        if 1 <= num <= N:
            if result[num-1] < last_update:
                result[num-1] = last_update
            result[num-1] += 1
            max_counter = max(max_counter, result[num-1])
        else:
            last_update = max_counter

    for i in range(N):
        if result[i] < last_update:
            result[i] = last_update

    return result