from collections import defaultdict
from collections import deque
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        checker = Counter(s)
        for i in range(len(s)):
            if s[i] not in visited:
                while stack:
                    if checker[stack[-1]] > 0 and stack[-1] > s[i]:
                        visited.discard(stack[-1])
                        stack.pop()
                    else:
                        break
                stack.append(s[i])
                visited.add(s[i])
                checker[s[i]] -= 1
            else:
                checker[s[i]] -= 1
        return "".join(stack)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # occurrence = defaultdict(list)
        # returned = deque([])
        # returned.insert(0, "a")
        # returned.insert(0, "b")
        # print(list(returned))
        # for i in range(len(s)):
        #     occurrence[s[i]].append(i)
        # print(occurrence)
        # new_s = list(set(list(s)))
        # new_s.sort()
        # if "".join(new_s) in s:
        #     return "".join(new_s)
        
        
            