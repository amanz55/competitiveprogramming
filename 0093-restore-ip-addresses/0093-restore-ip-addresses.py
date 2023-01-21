class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []
        
        def backtrack(i,integer):
            
            if i==len(s):
                if len(integer)==4:
                    answer.append( '.'.join(map(str,integer)) )
                return
            
            if integer[-1]!=0 and integer[-1]*10+int(s[i]) <= 255:
                lastItem = integer[-1]
                integer[-1] = lastItem*10+int(s[i])
                backtrack(i+1, integer)
                integer[-1] = lastItem
            
            if len(integer)<4:
                backtrack(i+1,integer + [int(s[i])])
        
        backtrack(1,[int(s[0])])
        return answer
        
        
        
        
#         answer = []
        
        
        
        
#         def backtrack(idx, integer, temp, words):
#             print(integer)
#             if idx >= len(s):
#                 if words >= 3:
#                     answer.append(temp)
#                 return 
#             elif int(integer) == 0:
#                 backtrack(idx + 1, s[idx], temp + [s[idx]], words + 1 )
#             elif int(integer + s[idx]) > 255:
#                 backtrack(idx + 1, "0", temp + ["."], words + 1)
#             else:
#                 backtrack(idx + 1, integer + s[idx], temp + [s[idx]], words )
#                 backtrack(idx + 1, "0", temp + ["."], words + 1)
                
                
                
                
#         backtrack(0, "0", [], 0)
#         return answer