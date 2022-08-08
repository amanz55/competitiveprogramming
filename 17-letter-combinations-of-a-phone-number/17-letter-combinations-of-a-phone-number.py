class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits = list(map(int, digits))
        result = []
        mapp = {
            2 : ["a", "b", "c"],
            3 : ["d", "e", "f"],
            4 : ["g", "h", "i"],
            5 : ["j", "k", "l"],
            6 : ["m", "n", "o"],
            7 : ["p", "q", "r", "s"],
            8 : ["t", "u", "v"],
            9 : ["w", "x", "y", "z"]
        }
        
        def dfs(idx, word):
            num2 = digits[idx]
            for child in mapp[num2]:
                if idx == (len(digits) - 1):
                    result.append(word+child)
                else:
                    dfs(idx + 1, word + child)
                        
        if digits:dfs(0, "")
        
        return result
            