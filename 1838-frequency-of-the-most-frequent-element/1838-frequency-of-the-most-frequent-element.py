class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        maximum = 1
        nums.sort()
        left = 0
        running = nums[0]
        for right in range(1, len(nums)):
            expected = nums[right] * ( right - left + 1 )
            running += nums[right]
            while expected - running > k:
                running -= nums[left]
                left += 1
                expected = nums[right] * ( right - left + 1 )
            maximum = max(maximum, right - left + 1)
        
        return maximum
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         nums.sort(reverse=True)
#         start, end = 0, 0
#         maxfreq = 1
        
#         while end < len(nums):
#             if nums[start] - nums[end] > k:
#                 maxfreq = max(maxfreq, end - start)
#                 k += (end - start - 1) * (nums[start] - nums[start + 1])
#                 start += 1
#             else:
#                 k -= nums[start] - nums[end]
#                 end += 1
#             maxfreq = max(maxfreq, end - start)
#         return maxfreq
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # nums.sort()
        # differences=0
        # mymax=0
        # for i in range(len(nums)-1,0,-1):
        #     sums=0
        #     count=0
        #     j=i-1
        #     while j>-1:
        #         sums += nums[i]-nums[j]
        #         if sums>k:
        #             break
        #         count+=1
        #         j-=1
        #     mymax=max(count,differences)
        #     differences=mymax
        #     if mymax >= i:
        #         break
        # return mymax + 1
                
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # differences=[]
        # for i in range(len(nums)-1):
        #     var=[]
        #     var.append(nums[i])
        #     var.append(nums[i+1])
        #     var.append(nums[i+1]-nums[i])
        #     differences.append(var)
        # print(differences)    
        # differences=sorted(differences, key=lambda x: x[2]) 
        # print(differences)
        # 1,2,3,4,7,9,10
        # finals=[]
        # finals.append(differences[0][0])
        # for j in range(len(differences)):
        #     finals.append(differences[j][1])
        # print(finals)    
            