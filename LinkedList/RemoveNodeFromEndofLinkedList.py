# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Stupid solution
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         curr, prev = head, None
#         while curr:
#             temp1 = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp1
#         #The head should be prev
#         pointer = prev
#         if n == 1:
#             prev = pointer.next
#         elif n == 2:
#             pointer.next = pointer.next.next
#         else:
#             for _ in range(n-2):
#                 pointer = pointer.next
#             pointer.next = pointer.next.next
#         
#         curr , prev1 = prev , None
#         while curr:
#             temp = curr.next
#             curr.next = prev1
#             prev1 = curr
#             curr = temp
#         return prev1

# Two Pointer
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head
        for _ in range(n):
            right = right.next
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

