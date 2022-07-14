class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        newguards = set(list(map(tuple, guards)))
        newwalls = set(list(map(tuple, walls)))
        guarded = set()
        
#         for i in range(m):
#             k = 0
#             for j in range(n):
#                 if (i, j) in newguards:
#                     k = 1
#                 elif (i, j) in newwalls:
#                     k = 0
#                 elif k == 1:
#                     guarded.add((i, j))
        
#         for i in range(m - 1, -1, -1):
#             k = 0
#             for j in range(n - 1, -1, -1):
#                 if (i, j) in newguards:
#                     k = 1
#                 elif (i, j) in newwalls:
#                     k = 0
#                 elif k == 1:
#                     guarded.add((i, j))
                    
#         for i in range(n):
#             k = 0
#             for j in range(m):
#                 if (j, i) in newguards:
#                     k = 1
#                 elif (j, i) in newwalls:
#                     k = 0
#                 elif k == 1:
#                     guarded.add((j, i))
                    
#         for i in range(n - 1, -1, -1):
#             k = 0
#             for j in range(m - 1, -1, -1):
#                 if (j, i) in newguards:
#                     k = 1
#                 elif (j, i) in newwalls:
#                     k = 0
#                 elif k == 1:
#                     guarded.add((j, i))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        for i in guards:
            j, k = i[0], i[1]
            while j - 1 >= 0:
                if (j - 1, k) not in newguards and (j - 1, k) not in newwalls:
                    guarded.add((j - 1, k))
                    j -= 1
                else:
                    break
            j, k = i[0], i[1]
            while k - 1 >= 0:
                if (j, k - 1) not in newguards and (j, k - 1) not in newwalls:
                    guarded.add((j, k - 1))
                    k -= 1
                else:
                    break
            j, k = i[0], i[1]
            while j + 1 < m:
                if (j + 1, k) not in newguards and (j + 1, k) not in newwalls:
                    guarded.add((j + 1, k))
                    j += 1
                else:
                    break
            j, k = i[0], i[1]
            while k + 1 < n:
                if (j, k + 1) not in newguards and (j, k + 1) not in newwalls:
                    guarded.add((j, k + 1))
                    k += 1
                else:
                    break
        return (m * n) - (len(guarded) + len(guards) + len(walls))