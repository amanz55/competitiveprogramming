from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        freq = Counter(changed)
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        original = []
        
        for num in changed:
            if freq[num] > 0 and freq[num * 2] > 0:
                freq[num] -= 1
                freq[num * 2] -= 1
                original.append(num)
            elif num % 2 != 0:
                return []
            elif num // 2 not in freq:
                return []
            
        return original
        
        
        """
        1,3,4,2,6,8
        1,2,3,4,6,8
        1 - 0
        2 - 0
        3 - 1
        4 - 1
        6 - 1
        8 - 1
        [1,]
        
        
        """
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # odds=[]
        # evens=[]
        # original=[]
        # if len(changed)%2!=0:
        #     return []
        # changed.sort()
        # for i in changed:
        #     if i%2==0:
        #         evens.append(i)
        #     else:
        #         if 2*i in changed:
        #             original.append(i)
        #             changed.remove(2*i)
        #         else:
        #             return []
        # if len(evens)%2 != 0:
        #     return []
        # else:
        #     while len(evens)>0:
        #         if evens[-1]//2 in evens:
        #             original.append(evens[-1]//2)
        #             evens.remove(evens[-1]//2)
        #             evens.pop()
        #         else:
        #             return []
        #     return original
            
        