"""
Task: Min Max Division
- Divide array A into K blocks and minimize the largest sum of any block.
"""

def solution(K, M, A):
    beg = max(A)
    end = sum(A)
    large_sum = end
    while beg <= end:
        mid = (beg + end) // 2
        if check(A, K, mid):
            large_sum = mid
            end = mid - 1
        else:
            beg = mid + 1
    return large_sum
        
def check(A, K, mid):
    total_sum = 0
    blocks = 1
    for num in A:
        total_sum += num
        if total_sum > mid:
            blocks += 1
            total_sum = num
        if blocks > K:
            return False
    return True