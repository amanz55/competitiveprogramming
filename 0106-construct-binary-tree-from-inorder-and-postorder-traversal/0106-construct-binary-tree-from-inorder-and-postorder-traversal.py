# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indexer = {}
        for idx, num in enumerate(postorder):
            indexer[num] = idx
            
            
            
        def build(values):
            if not values:
                return None
            if len(values) == 1:
                node = TreeNode(values[0])
                return node
            
            maximum = [-inf, -inf]
            for i, val in enumerate(values):
                maximum = max(maximum, [indexer[val], i])
            i = maximum[1]
            node = TreeNode(values[i])
            node.left = build(values[:i])
            node.right = build(values[i + 1:])
            
            return node
        
        return build(inorder)
                
            
            
            
                
            