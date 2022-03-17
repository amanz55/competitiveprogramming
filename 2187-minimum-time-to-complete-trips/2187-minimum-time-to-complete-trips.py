class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = 0
        right = max(time) * totalTrips
        ans = 0
        
        def trips(midd):
            sums = 0
            for i in time:
                sums += midd // i
            return sums
        
        while left <= right:
            mid = (right + left) // 2
            if trips(mid) < totalTrips:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
                
        return ans
                
            