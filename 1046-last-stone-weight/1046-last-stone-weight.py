import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heapq.heapify(stones)
        while len(stones) > 0:
            temp = heapq.nsmallest(2, stones)
            if len(temp) == 1:
                return -1 * temp[0]
            if temp[0] == temp[1]:
                heapq.heappop(stones)
                heapq.heappop(stones)
            else:
                heapq.heappop(stones)
                heapq.heappop(stones)
                heapq.heappush(stones, -1 * abs(temp[0] - temp[1]))
        return 0
        