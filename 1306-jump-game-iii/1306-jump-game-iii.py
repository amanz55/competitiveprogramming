from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        myque = deque([start])
        
        
        while myque:
            size = len(myque)
            for i in range(size):
                idx = myque.popleft()
                if idx in visited:
                    continue
                if arr[idx] == 0:
                    return True
                visited.add(idx)
                
                if idx + arr[idx] < len(arr) and idx - arr[idx] >= 0:
                    myque.append(idx + arr[idx])
                    myque.append(idx - arr[idx])
                elif idx + arr[idx] < len(arr):
                    myque.append(idx + arr[idx])
                elif idx - arr[idx] >= 0:
                    myque.append(idx - arr[idx])
                else:
                    continue
                    
        return False