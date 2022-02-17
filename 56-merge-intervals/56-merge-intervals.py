class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        finalret = []
        i = 0
        
        if len(intervals) == 1:
            return intervals
        
        if intervals[1][0] <= intervals[0][1]:
            var = [intervals[0][0], max( intervals[0][1],intervals[1][1] )]
            finalret.append(var)
            i = 2
        else:
            finalret.append(intervals[0])
            i = 1
        
        while i < len(intervals):
            
            if intervals[i][0] <= finalret[-1][1]:
                var = [finalret[-1][0], max( finalret[-1][1],intervals[i][1] )]
                finalret.pop()
                finalret.append(var)
                i += 1
            else:
                finalret.append(intervals[i])
                i += 1
        
        
        return finalret
        