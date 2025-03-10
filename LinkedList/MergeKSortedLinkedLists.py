# Definition for singly-linked list.
from torchgen.selective_build.operator import merge_debug_info


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergelist = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergelist.append(self.mergeTwoList(l1, l2))
            lists = mergelist
        return lists[0]

    def mergeTwoList(self, l1, l2):
        dummy = ListNode(-1)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next
