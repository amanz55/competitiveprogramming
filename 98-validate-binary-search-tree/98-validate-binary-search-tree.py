# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traversed = []
        
        def traverse(rt):
            if not rt:
                return
            traverse(rt.left)
            
            traversed.append(rt.val)
            
            traverse(rt.right)
            
        traverse(root)
        
        if sorted(list(set(traversed))) == traversed:
            return True
        else:
            return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def validate(rt):
#             if not rt or (not rt.left and not rt.right):
#                 return True
#             if rt.left and rt.right:
#                 if rt.val < rt.right.val and rt.val > rt.left.val:
#                     return validate(rt.left) and validate(rt.right)
#                 else:
#                     return False
#             elif rt.left:
#                 if rt.val > rt.left.val:
#                     return validate(rt.left)
#                 else:
#                     return False
#             elif rt.right:
#                 if rt.val < rt.right.val:
#                     return validate(rt.right)
#                 else:
#                     return False
                
                
#         return validate(root)
            
            
        