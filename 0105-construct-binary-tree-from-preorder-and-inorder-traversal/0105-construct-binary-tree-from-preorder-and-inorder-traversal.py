# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexer = {}
        j = 0
        
        for i, val in enumerate(inorder):
            indexer[val] = i
            
        def build(left, right):
            nonlocal j
            if left > right:
                return None
            num = preorder[j]
            
            node = TreeNode(num)
            j += 1
            node.left = build(left, indexer[num] - 1)
            node.right = build(indexer[num] + 1, right)
            
            return node
        
        return build(0, len(preorder) - 1)