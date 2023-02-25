class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        queue = deque()
        for i, val in enumerate(tickets):
            queue.append((val, i))
        
        
        while queue:
            val, idx = queue.popleft()
            val -= 1
            count += 1
            if val != 0:
                queue.append((val, idx))
            elif idx == k and val == 0:
                return count
            