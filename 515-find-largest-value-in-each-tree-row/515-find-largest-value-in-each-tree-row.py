# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        arr = []
        if not root:
            return []
        
        queue = deque([root])
        while queue:
            max_elt = -float('inf')
            size = len(queue)
            for i in range(size):
                cur_elt = queue.popleft()
                max_elt = max(max_elt, cur_elt.val)
                if cur_elt.left:
                    queue.append(cur_elt.left)
                if cur_elt.right:
                    queue.append(cur_elt.right)
            arr.append(max_elt)
            
        return arr

































# class Solution:
#     def largestValues(self, root: Optional[TreeNode]) -> List[int]:
#         myque = deque([root])
#         if root:
#             result = [root.val]
#         else:
#             return []
        
#         while myque:
#             size = len(myque)
#             for i in range(size):
#                 rt = myque.popleft()
#                 if rt.left and rt.right:
#                     myque.append(rt.left)
#                     myque.append(rt.right)
#                 elif rt.left:
#                     myque.append(rt.left)
#                 elif rt.right:
#                     myque.append(rt.right)
#                 else:
#                     continue
#             if len(myque) != 0:
#                 maxim = myque[0].val
#                 for i in myque:
#                     if i.val > maxim:
#                         maxim = i.val
#                 result.append(maxim)
                
#         return result