"""
Task: Odd Occurrences In Array
- Find value that occurs in odd number of elements.
"""

from collections import Counter

# Time complexity: O(N)
def solution(A):
    count_dic = dict(Counter(A))
    for key, val in count_dic.items():
        if val % 2 == 1:
            return key