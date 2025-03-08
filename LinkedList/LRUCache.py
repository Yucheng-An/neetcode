class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mapCache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self,node):
        prev, next = node.prev, node.next
        prev.next , next.prev = next, prev
        
    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.mapCache:
            self.remove(self.mapCache[key])
            self.insert(self.mapCache[key])
            return self.mapCache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapCache:
            self.remove(self.mapCache[key])
        self.mapCache[key] = Node(key,value)
        self.insert(self.mapCache[key])
        
        if len(self.mapCache)>self.cap:
            rem = self.left.next
            self.remove(rem)
            del self.mapCache[rem.key]
                
