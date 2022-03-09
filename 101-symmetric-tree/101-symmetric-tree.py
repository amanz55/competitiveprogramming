from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        myque = deque([root])
        level = 0
        
        while myque:
            size = len(myque)
            for i in range(size):
                rt = myque.popleft()
                if rt:
                    myque.append(rt.left)
                    myque.append(rt.right)
                else:
                    continue
            
            start, end = 0, len(myque) - 1
            while start < end:
                if myque[start] == None or myque[end] == None:
                    if myque[start] == myque[end] == None:
                        start += 1
                        end -= 1
                        continue
                    else:
                        return False
                elif myque[start].val != myque[end].val:
                    return False
                start += 1
                end -= 1
                
        return True
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         traversedleft = []
#         traversedright = []
#         levelLeft = 1
#         levelright = 1
        
#         def gotoleft(r1,levelleft):
#             if r1 is None:
#                 return levelleft
#             levelleft += 1
#             return gotoleft(r1.left,levelleft)
            
#         def gotoright(r2,levelright):
#             if r2 is None:
#                 return levelright
#             levelright += 1
#             return gotoright(r2.right,levelright)
        
#         if gotoleft(root,levelLeft) != gotoright(root,levelright):
#             return False
        
#         def traverse(r):
#             if r is None:
#                 return
            
#             traverse(r.left)
        
#             traversedleft.append(r.val)
            
#             traverse(r.right)
        
#         def travers(r):
#             if r is None:
#                 return
            
#             travers(r.left)
        
#             traversedright.append(r.val)
            
#             travers(r.right)
              
#         traverse(root.left)
#         travers(root.right)
#         print(traversedleft)
#         print(traversedright)
        
#         if list(reversed(traversedleft)) == traversedright:
#             return True
#         else:
#             return False


        