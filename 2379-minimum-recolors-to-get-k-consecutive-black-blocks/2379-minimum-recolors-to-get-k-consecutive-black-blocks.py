class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = blocks[:k].count("W")
        answer = count
        left = 0
        
        for r in range(k, len(blocks)):
            count += blocks[r] == "W"
            count -= blocks[left] == "W"
            answer = min(answer, count)
            left += 1
            
        return answer
        