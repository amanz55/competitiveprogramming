class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[i+1] and nums[i]!='_':
                    nums.remove(nums[i+1])
                    nums.append('_')
                    count+=1
                else:
                    break
        return (len(nums)-count)
