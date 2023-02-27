"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_dict = {}
        new = Node(head.val)
        curr = new
        node_dict[head] = curr
        head = head.next
        
        
        while head:
            node = Node(head.val)
            curr.next = node
            curr = curr.next
            node_dict[head] = node
            head = head.next
            
        for key, value in node_dict.items():
            if key.random == None:
                value.random = None
            else:
                value.random = node_dict[key.random]
        return new
            