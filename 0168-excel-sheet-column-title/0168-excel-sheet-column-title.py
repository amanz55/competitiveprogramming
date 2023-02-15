class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = []
        
        while columnNumber:
            result = (columnNumber - 1)
            res = result % 26
            answer.append(chr(res + 65))
            columnNumber = result // 26
            
        return "".join(answer[::-1])