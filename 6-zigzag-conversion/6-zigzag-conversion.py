class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = []
        s = list(s)
        for i in range(numRows):
            answer.append([])  
        flag = True
        idx = 0
        l = len(s)
        while idx < l:
                for j in range(len(answer)):
                    if idx < l:
                        answer[j].append(s[idx])
                        idx += 1
                for k in range(len(answer) - 2, 0, -1):
                    if idx < l:
                        answer[k].append(s[idx])
                        idx += 1
                # for o in range(1, len(answer), 1):
                #     if idx < l:
                #         answer[o].append(s[idx])
                #         idx += 1
                # for k in range(len(answer) - 2, 0, -1):
                #     if idx < l:
                #         answer[k].append(s[idx])
                #         idx += 1
        for i in range(len(answer)):
            answer[i] = "".join(answer[i])
        return "".join(answer)
            
        
        