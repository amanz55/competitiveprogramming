class Node:
    def __init__(self, val, key, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = {}
        self.length = 0
        self.head = None
        self.tail = None
        

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        
        node = self.key_node[key]
        if node != self.tail:
            p = node.prev
            n = node.next
            node.next = None
            if p:
                p.next = n
            else:
                self.head = n
            n.prev = p
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self.get(key)
        
        else:
            node = Node(value, key)
            self.key_node[key] = node
            
            if self.length == self.capacity:
                bey = self.head.key
                n = self.head.next
                if n:
                    n.prev = None
                self.head = n
                self.key_node.pop(bey)


            if not self.head:
                self.head = node
                self.tail = node
                self.length = 1

            else:  
                self.tail.next = node
                node.prev = self.tail
                self.length = min(self.length + 1, self.capacity)
                self.tail = node
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)