class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        returned = [points[0]]
        max_arrow = 1
        for i in range(1,len(points)):
            if points[i][0] <= returned[-1][1]:
                returned.append([points[i][0], min(returned[-1][1], points[i][1])])
            else:
                returned.append(points[i])
                max_arrow += 1
        return max_arrow