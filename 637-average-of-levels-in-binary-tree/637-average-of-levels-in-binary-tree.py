# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        myque = deque([root])
        result = [root.val]
        
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
                sums = 0
                for i in myque:
                    sums += i.val
                result.append(sums/len(myque))
                
        return result