# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, row, col):
        if not node:
            return
        self.dictionary[col].append((row, node.val))
        self.dfs(node.left, row + 1, col - 1)
        self.dfs(node.right, row + 1, col + 1)
        
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dictionary = defaultdict(list)
        self.dfs(root, 0, 0)
        refs = sorted(self.dictionary)
        answer = []
        for ref in refs:
            ref = sorted(self.dictionary[ref])
            temp = []
            for el in ref:
                temp.append(el[-1])
            answer.append(temp)
        return answer
        