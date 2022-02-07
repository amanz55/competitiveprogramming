# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        prev=head
        temp=head
        head=head.next
        while head:
            if head.val==prev.val:
                prev.next=head.next
                head=head.next
            else:
                prev=prev.next
                head=head.next
        return temp
        