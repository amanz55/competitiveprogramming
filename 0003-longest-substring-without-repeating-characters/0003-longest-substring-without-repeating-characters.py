class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        visited = set()
        longest = 0
        
        while right < len(s):
            if s[right] not in visited:
                visited.add(s[right])
            else:
                while s[left] != s[right]:
                    visited.remove(s[left])
                    left += 1
                    
                left += 1
            right += 1
            longest = max(longest, right - left)
                
        return longest