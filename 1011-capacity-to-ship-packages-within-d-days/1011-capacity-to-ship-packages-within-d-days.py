class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def countDays(capacity):
            weight = count = 0
            for i in weights:
                weight += i                
                if weight > capacity:
                    count += 1
                    weight = i
            return count + 1
        
        min_weight = 0
        
        left = max(weights)
        right = sum(weights)
        
        while left <= right:
            mid = (left + right) // 2
            d = countDays(mid)
            if d <= days:
                min_weight = mid
                right = mid  - 1
            else:
                left = mid + 1
        return min_weight