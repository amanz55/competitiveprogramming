class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
            
        stack = []
        
        for i in range(len(temperatures)):
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                result[idx] = i - idx
                
            stack.append(i)
            
            
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         start = 0
#         lead = 1
#         myStack = []
        
#         while start < len(temperatures) - 1:
                
#             if temperatures[lead] > temperatures[start]:
#                 myStack.append(lead-start)
#                 start += 1
#                 lead = start + 1
#             else:
#                 lead += 1
#                 if lead == len(temperatures):
#                     myStack.append(0)
#                     start += 1
#                     lead = start + 1
                    
#         myStack.append(0)
        
#         return myStack
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         myList = []
#         for i in range(len(temperatures)):
#             var = True
#             for j in range(i + 1, len(temperatures)):
#                 if temperatures[j] > temperatures[i]:
#                     myList.append(j - i)
#                     var = False
#                     break
#             if var == True:
#                 myList.append(0)
                
#         return myList
                
        