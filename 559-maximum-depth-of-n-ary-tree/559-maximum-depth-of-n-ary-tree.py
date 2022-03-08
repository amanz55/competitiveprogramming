from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self.maxdepth = 0
        
        def godeep(root, runmax):
            if len(root.children) == 0:
                self.maxdepth = max(self.maxdepth, runmax)
            for i in root.children:
                godeep(i, runmax + 1)
                
        godeep(root, 1)
        
        return self.maxdepth
        
        
        
#         myque = deque([root])
#         traversed = []
        
#         while myque:
#             for i in myque[0].children:
#                 myque.append(i)
#             traversed.append(myque.popleft().val)
#         print(traversed)
            
            
        