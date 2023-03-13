class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        answer = []
        
        def backtrack(num, list_, k, n):
            if len(list_) == k:
                answer.append(list_)
                return 
            
            if len(list_) > k or num > n:
                return
            
            for idx in range(num + 1, n + 1):
                backtrack(idx, list_ + [idx], k, n)
                
        backtrack(0, [], k, n)
        return answer