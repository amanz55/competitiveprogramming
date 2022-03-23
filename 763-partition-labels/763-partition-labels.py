class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i = 0
        res = []
        
        
        while i < len(s):
            best = i
            for j in range(i + 1, len(s)):
                if s[j] == s[i]:
                    best = max(best, j)
            absmax = best
            k = i + 1
            while k < best:
                bst = -1
                for j in range(k + 1, len(s)):
                    if s[j] == s[k]:
                        bst = max(bst, j)
                absmax = max(absmax, bst)
                best = absmax
                k += 1
            res.append(absmax - i + 1)
            i = absmax + 1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = []
        # while i < len(s):
        #     target = s[i]
        #     left = i
        #     right = len(s) - 1
        #     val = 0
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         print(mid)
        #         if s[mid] == target:
        #             val = mid
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        #     print("heyyyy")
        #     best = val
        #     for j in range(i + 1, val):
        #         target = s[j]
        #         left = j
        #         right = len(s) - 1
        #         vl = 0
        #         while left <= right:
        #             mid = left + (right - left) // 2
        #             if s[mid] == target:
        #                 vl = mid
        #                 left = mid + 1
        #             else:
        #                 right = mid - 1
        #         best = max(best, vl)
        #     res.append(best - i + 1)
        #     i = best + 1
        # return res