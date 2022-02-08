class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arr=[]
        sums1=0
        sums2=0
        arr2=[]
        leftmost=-1
        arr.append(sums1)
        for i in range(1,len(nums)):
            sums1+=nums[i-1]
            arr.append(sums1)
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                if sums2==arr[i]:
                    leftmost=i
                arr2.append(sums2)
                continue
            sums2+=nums[i+1]
            if sums2==arr[i]:
                leftmost=i
            arr2.append(sums2)
        return leftmost
            
        