class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            changed=False
            if nums2.index(i)==len(nums2)-1:
                ans.append(-1)
                continue
            for j in range(nums2.index(i)+1,len(nums2)):
                if nums2[j]>i:
                    ans.append(nums2[j])
                    changed=True
                    break
            if j==len(nums2)-1 and changed==False:
                ans.append(-1)
        return ans
        