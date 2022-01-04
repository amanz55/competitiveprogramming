class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(len(nums1)-len(nums2),len(nums1)):
            nums1[i]=nums2[i-len(nums1)+len(nums2)]
        nums1.sort()
        
