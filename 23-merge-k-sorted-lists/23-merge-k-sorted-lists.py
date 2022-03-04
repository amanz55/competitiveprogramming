# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush,heappop

class Solution:
    def mergeKLists(self, matrix: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for i in range(len(matrix)):
            if matrix[i] :
                temp = (matrix[i].val,i)
                matrix[i] = matrix[i].next
                heappush(heap,temp)
                
        curr = dummy = ListNode()
        
        while(heap):
            val,i = heappop(heap)
            
            curr.next = ListNode(val)
            curr = curr.next
            if matrix[i]:
                heappush(heap,(matrix[i].val,i))
                matrix[i] = matrix[i].next
    
        return dummy.next
        
        
#         def findSmallest(matrix: List[List[int]]):
#             minimum = []
#             for i in range(len(matrix)):
#                 temp = (matrix[i].val,i,0)
#                 minimum.append(temp)
#             matrix = minimum.copy()
#             heapq.heapify(minimum)
#             for i in range(len(matrix) - 1):
#                 finished.append(minimum[0][0])
#                 val = 0
#                 mytuple = heapq.heappop(minimum)
#                 col = mytuple[2] + 1
#                 if col == len(matrix):
#                     val = float('+inf')
#                 else:
#                     val = matrix[mytuple[1]][col]
#                 heapq.heappush(minimum, (val, mytuple[1], col))
                
#         findSmallest(lists)
#         print(finished)
        