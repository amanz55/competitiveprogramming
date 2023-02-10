class Solution:
    def find(self, nums1, nums2, k):
        ans = -1
        left = 0
        right = len(nums1) - 1
        
        
        while left <= right:
            mid = left + (right - left) // 2
            
            idx1 = bisect.bisect_left(nums2, nums1[mid])
            idx2 = bisect.bisect_right(nums2, nums1[mid])
                
            num_less1 = (mid + idx1)
            num_less2 = (mid + idx2)
            
            if num_less1 <= k <= num_less2:
                return nums1[mid]
            
            elif num_less1 < k:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return -inf
        
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        
        temp = n + m
        k = (temp) // 2
        
        m1 = self.find(nums1, nums2, k)
        if m1 == -inf:
            m1 = self.find(nums2, nums1, k)
        
        m2 = m1
        if temp % 2 == 0:
            
            m2 = self.find(nums1, nums2, k - 1)
            if m2 == -inf:
                m2 = self.find(nums2, nums1, k - 1)
        
        ans = (m1 + m2) / 2 
        return ans