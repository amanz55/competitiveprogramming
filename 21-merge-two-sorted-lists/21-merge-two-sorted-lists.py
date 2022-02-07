# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==list2==None:
            return None
        arr=[]
        while list1:
            arr.append(list1)
            list1=list1.next
        while list2:
            arr.append(list2)
            list2=list2.next
        arr = sorted(arr, key=lambda x: x.val)
        temp = arr[0]
        for i in range(len(arr)-1):
            arr[i].next=arr[i+1]
        arr[-1].next=None
        return temp
        