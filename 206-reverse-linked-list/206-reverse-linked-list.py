# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head)
            head=head.next
        if len(arr)==0:
            return None
        temp=arr[-1]
        for i in range(len(arr)-1,0,-1):
            arr[i].next=arr[i-1]
        arr[0].next=None
        return temp
        
        
        