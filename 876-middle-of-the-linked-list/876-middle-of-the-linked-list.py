# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while(fast!=None and fast.next!=None): 
            fast=fast.next.next
            slow=slow.next
        return slow
        # length=0
        # iterator=0
        # while(head!=None):
        #     length+=1
        #     head=head.next
        # while(temp!=None):
        #     iterator+=1
        #     if(iterator==length//2+1):
        #         return temp
        #     temp=temp.next
            
        