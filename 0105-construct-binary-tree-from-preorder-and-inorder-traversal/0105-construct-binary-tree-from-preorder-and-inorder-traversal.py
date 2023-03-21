# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexer = {}
        
        for i, val in enumerate(preorder):
            indexer[val] = i
            
        def build(values):
            if not values:
                return None
            
            if len(values) == 1:
                node = TreeNode(values[0])
                return node
            
            minimum = [inf, inf]
            
            for idx, value in enumerate(values):
                minimum = min(minimum, [indexer[value], idx])
                
            i = minimum[1]
            
            node = TreeNode(values[i])
            node.left = build(values[:i])
            node.right = build(values[i + 1:])
            
            return node
        
        return build(inorder)