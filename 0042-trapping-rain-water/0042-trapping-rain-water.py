class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        answer = 0
        
        for i in range(len(height)):
            
            while stack and height[i] >= stack[-1][1]:
                idx, heigh = stack.pop()
                if stack:
                    h = min(stack[-1][1], height[i]) - heigh
                    w = i - stack[-1][0] - 1
                    answer += h * w
            stack.append([i, height[i]])
            
        return answer