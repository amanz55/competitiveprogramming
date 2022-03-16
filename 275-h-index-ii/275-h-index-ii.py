class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        if citations == [0] * len(citations):
            return 0
        h = 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if citations[mid] == len(citations) - mid:
                return citations[mid]
                
            elif citations[mid] < len(citations) - mid:
                left = mid + 1
            else:
                h = max(h, len(citations) - mid)
                right = mid - 1
        return h