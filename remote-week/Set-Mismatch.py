class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        var=[]
        nums.sort()
        for i in range(len(nums)):
            if nums.count(nums[i])>1:
                var.append(nums[i])
                nums.remove(nums[i])
                print(len(nums))
                for i in range(len(nums)):
                    if nums[i]!=i+1:
                        var.append(i+1)
                        break
                    elif i==len(nums)-1:
                        var.append(i+2)
                        break
                break
        return var        
        
