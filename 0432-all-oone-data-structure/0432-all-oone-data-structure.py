class Node:
    def __init__(self, val = "", prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
        
        
class AllOne:

    def __init__(self):
        self.count = defaultdict(int)
        self.node_idx = defaultdict(None)
        self.references = defaultdict(None)
        
        
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.node_idx[0] = self.head
    
        
    def inc(self, key: str) -> None:
        node = self.references.get(key)
        value = self.count[key] + 1
        self.count[key] = value
        
        if not node:
            node = Node(key)
            self.references[key] = node
        else:
            #delete
            temp = node.prev
            if self.node_idx[value - 1] == node:
                if self.count[node.prev.val] == (value - 1):
                    self.node_idx[value - 1] = node.prev
                else:
                    self.node_idx.pop(value - 1)
                    
            p = node.prev
            n = node.next
            if p:
                p.next = n
                n.prev = p
            
            node.prev = None
            node.next = None
        
        #add
        if value in self.node_idx:
            last = self.node_idx[value]
            p = last.prev
            last.prev = node
            p.next = node
            node.next = last
            node.prev = p
        
        else:
            last = self.node_idx.get(value - 1)

            if not last:
                last = temp
                
            n = last.next
            last.next = node
            node.prev = last
            node.next = n
            n.prev = node
            self.node_idx[value] = node
            
    def dec(self, key: str) -> None:    
        node = self.references.get(key)
        value = self.count[key] - 1
        self.count[key] = value
        temp = node.prev
        
       #delete
        if self.node_idx[value + 1] == node:
            if self.count[node.prev.val] == (value + 1):
                self.node_idx[value + 1] = node.prev
            else:
                self.node_idx.pop(value + 1)

        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

        node.prev = None
        node.next = None
        
        #add
        if value in self.node_idx:
            last = self.node_idx[value]
            
            if value != 0:
                p = last.prev
                p.next = node
                last.prev = node
                node.next = last
                node.prev = p
        
        else:
            last = self.node_idx.get(value - 1)

            if not last:
                last = temp
                
            n = last.next
            last.next = node
            node.prev = last
            node.next = n
            n.prev = node
            self.node_idx[value] = node

    def getMaxKey(self) -> str:
        return self.tail.prev.val
        

    def getMinKey(self) -> str:
        return self.head.next.val
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()