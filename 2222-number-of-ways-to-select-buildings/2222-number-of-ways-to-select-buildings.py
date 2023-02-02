class Solution:
    def numberOfWays(self, s: str) -> int:
        left_count = list(map(int, '0' + s))
        length = len(left_count)
        ones = sum(left_count)
        
        for i in range(1, length):
            left_count[i] += left_count[i-1]
        
        answer = 0
        length -= 1
        for i in range(1, length-1):
            left, right = 0, 0
            if s[i] == '1':
                left = i - left_count[i]
                right = ones - left_count[i] - 1
                right = length - i - 1 - right
                 
            else:
                left = left_count[i]
                right = ones - left
            
            answer += (left * right)
        return answer