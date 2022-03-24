# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        myque = deque([root])
        if root:
            result = [root.val]
        else:
            return []
        
        while myque:
            size = len(myque)
            for i in range(size):
                rt = myque.popleft()
                if rt.left and rt.right:
                    myque.append(rt.left)
                    myque.append(rt.right)
                elif rt.left:
                    myque.append(rt.left)
                elif rt.right:
                    myque.append(rt.right)
                else:
                    continue
            if len(myque) != 0:
                maxim = myque[0].val
                for i in myque:
                    if i.val > maxim:
                        maxim = i.val
                result.append(maxim)
                
        return result