
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        myMap = {None:None}
        while curr:
            copy = Node(curr.val)
            myMap[curr] = copy
            curr = curr.next
        curr = head

        while curr:
            copy = myMap[curr]
            copy.next = myMap[curr.next]
            copy.random = myMap[curr.random]
            curr = curr.next
        return myMap[head]
