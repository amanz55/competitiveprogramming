# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

Author: Amanuel Alemayehu
Description: this is a code template that can also be used to get the levels and nodes in the specific levels as a level order traversal.

"""
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        level = 0
        answer =[]
        flag = True
        
        
        while queue:
            length = len(queue)
            temp = []
            for i in range(length):
                node = queue.popleft()
                temp.append(node.val)
                if (not node.left and node.right) or (not flag and node.left):
                    return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                else:
                    flag = False
            level += 1
            answer.append([temp,level])
        
        return True
        