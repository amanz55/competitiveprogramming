# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        fast = head
        slow = head
        prev = None
        count=0
        while fast:
            fast = fast.next
            count+=1
            if count>n:
                prev=slow
                slow=slow.next
        if count==n:
            return head.next
        prev.next=slow.next
        return head