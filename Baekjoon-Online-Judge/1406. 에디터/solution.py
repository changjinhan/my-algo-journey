# 1406. 에디터
# 연결 리스트 풀이: 메모리 96,864kb / 실행시간 904ms
# 스택 풀이: 메모리 42,832kb / 실행시간 284ms

import sys
sys.stdin = open("./sample_input.txt", "r")

T = int(input())

# 연결 리스트 풀이
# class Node:
#     def __init__(self, char):
#         self.char = char
#         self.prev = None
#         self.next = None

# class Cursor:
#     def __init__(self):
#         self.prev = None
#         self.next = None

# def left():
#     if cursor.prev:
#         cursor.next = cursor.prev
#         cursor.prev = cursor.prev.prev

# def right():
#     if cursor.next:
#         cursor.prev = cursor.next
#         cursor.next = cursor.next.next

# def backspace():
#     if cursor.prev:
#         if cursor.prev.prev and cursor.next:
#             cursor.prev.prev.next = cursor.next
#             cursor.next.prev = cursor.prev.prev
#         elif cursor.prev.prev and not cursor.next:
#             cursor.prev.prev.next = cursor.next
#         elif not cursor.prev.prev and cursor.next:
#             cursor.next.prev = cursor.prev.prev
        
#         cursor.prev = cursor.prev.prev        


# def push(char):
#     new_node = Node(char)
#     if cursor.prev and cursor.next:
#         new_node.prev = cursor.prev
#         new_node.next = cursor.next
#         cursor.prev.next = new_node
#         cursor.next.prev = new_node
#     elif not cursor.prev and cursor.next:
#         new_node.next = cursor.next
#         cursor.next.prev = new_node
#     elif cursor.prev and not cursor.next:
#         new_node.prev = cursor.prev
#         cursor.prev.next = new_node

#     cursor.prev = new_node


# for test_case in range(1, T+1):
#     text = input().strip()
#     N = len(text)
#     sentence = [Node(c) for c in text]
#     for i, c in enumerate(text):
#         if i == 0:
#             sentence[i].next = sentence[i+1]
#         elif i == N-1:
#             sentence[i].prev = sentence[i-1]
#         else:
#             sentence[i].prev = sentence[i-1]
#             sentence[i].next = sentence[i+1]

#     M = int(input())
#     cursor = Cursor()
#     cursor.prev = sentence[-1]
#     for _ in range(M):
#         command = input().split()
#         if command[0] == 'L':
#             left()
#         elif command[0] == 'D':
#             right()
#         elif command[0] == 'B':
#             backspace()
#         elif command[0] == 'P':
#             x = command[1]
#             push(x)
 
#     final_sentence = []
#     while cursor.prev:
#         left()
#     while cursor.next:
#         final_sentence.append(cursor.next.char)
#         right()
#     print(''.join(final_sentence))
    

# 스택 풀이
for test_case in range(1, T+1):
    left = list(input().strip())
    right = []
    
    M = int(input())
    for _ in range(M):
        command = input().strip()
        if command == 'L' and left:
            right.append(left.pop())
        elif command == 'D' and right:
            left.append(right.pop())
        elif command == 'B' and left:
            left.pop()
        elif command.startswith('P'):
            _, x = command.split()
            left.append(x)

    print(''.join(left + right[::-1]))








