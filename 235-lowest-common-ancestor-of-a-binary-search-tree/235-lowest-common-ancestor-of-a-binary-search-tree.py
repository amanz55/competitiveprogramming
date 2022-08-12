# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = []
        def findBst(node, target):
            if not node:
                return
            if node.val == target:
                self.res.append(node)
                return
            elif node.val > target:
                self.res.append(node)
                findBst(node.left, target)
            else:
                self.res.append(node)
                findBst(node.right, target)
        findBst(root, q.val)
        arr = self.res
        self.res = []
        findBst(root, p.val)
        x, y = len(arr), len(self.res)
        for i in range(min(x, y)):
            if arr[i].val != self.res[i].val:
                break
            abss = arr[i]
        return abss