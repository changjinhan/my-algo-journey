"""
Task: Odd Occurrences In Array
- Find value that occurs in odd number of elements.
"""

from collections import Counter

def solution1(A):
    count_dic = dict(Counter(A))
    for key, val in count_dic.items():
        if val % 2 == 1:
            return key

# Time complexity: O(N)
def solution2(A):
    result = 0
    for number in A:
        result ^= number # XOR operation 1)commutative: a⊕b=b⊕a, 2)associative (a⊕b)⊕c=a⊕(b⊕c)
    return result
