class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]
        nums = "".join(list(map(str, nums)))
        if int(nums) == 0:
            return str(0)
        return nums
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         nums=list(map(str,nums))
#         print(nums)
#         for i in range(1,len(nums)):
#             j=i-1
#             while j>-1:
#                 if nums[i][0]<nums[j][0]:
#                     break
#                 elif nums[i][0]==nums[j][0]:
#                     if len(nums[i])>len(nums[j]):
#                         num=int(nums[i][:len(nums[j])])
#                         if num<int(nums[j]):
#                             break
#                         elif num==int(nums[j]):
#                             if nums[i][len(nums[j])]<nums[j][0]:
#                                 break
#                             elif nums[j][len(nums[i])]==nums[j][0]:
#                                 break
#                             else:
#                                 j-=1
#                         else:
#                             if j==0:
#                                 break
#                             else:
#                                 j-=1
#                     elif len(nums[i])<len(nums[j]):
#                         num=int(nums[j][:len(nums[i])])
#                         if num>int(nums[i]):
#                             break
#                         elif num==int(nums[j]):
#                             if nums[j][len(nums[i])]>nums[j][0]:
#                                 break
#                             elif nums[j][len(nums[i])]==nums[j][0]:
#                                 if j==0:
#                                     break
#                                 else:
#                                     j-=1
#                             else:
#                                 j-=1
#                         else:
#                             if j==0:
#                                 break
#                             else:
#                                 j-=1
#                     else:
#                         if nums[i]<nums[j]:
#                             break
#                         else:
#                             if j==0:
#                                 break
#                             else:
#                                 j-=1
#                 else:
#                     j-=1
#             temp=nums[i]
#             del nums[i]
#             nums.insert(j+1,temp)
#         return "".join(nums)
                    
        