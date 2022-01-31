class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        myList=[]
        for i in range(len(nums)):
            if nums[i]==target:
                myList.append(i)
        return myList