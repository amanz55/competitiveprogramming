# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        myque = deque([root])
        result = [[root.val]]
        conv = False
        
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
                if conv == True:
                    val = []
                    for i in myque:
                        val.append(i.val)
                    result.append(val)
                    conv = False
                else:
                    val = []
                    for i in myque:
                        val.append(i.val)
                    result.append(list(reversed(val)))
                    conv = True
        return result
                