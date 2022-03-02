# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, node: Optional[ListNode]) -> Optional[ListNode]:
        
        if not node:
            return None
        
        if not node.next:
            return node
        
        if node.val != node.next.val:
            node.next = self.deleteDuplicates(node.next)
            return node
        
        while node.next and node.val == node.next.val:
            node = node.next
            
        return self.deleteDuplicates(node.next)
            
        