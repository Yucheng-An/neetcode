# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        prev, curr = None, head
        midp = None
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            if _ == k-1:
                curr.next = midp
            curr = temp
        prev, curr = None, midp
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            if _ == k-1:
                curr.next = midp
            curr = temp
        return prev
    
