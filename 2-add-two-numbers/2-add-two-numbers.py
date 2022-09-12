# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []
        temp = l1
        temp2 = l2
        while temp or temp2:
            if temp:
                arr1.append(temp.val)
                temp = temp.next
            if temp2:
                arr2.append(temp2.val)
                temp2 = temp2.next
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]
        arr1 = int("".join(map(str, arr1)))
        arr2 = int("".join(map(str, arr2)))
        result = arr1 + arr2
        result = list(str(result))
        result = result[::-1]
        result = list(map(int, result))
        head = ListNode()
        root = head
        for i in range(len(result)):
            root.val = result[i]
            if i < len(result) - 1:
                root.next = ListNode()
                root = root.next
        return head
        