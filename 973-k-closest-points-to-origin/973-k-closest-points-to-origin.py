class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            dis = sqrt(pow(points[i][0], 2) + pow(points[i][1], 2))
            var = [dis, i]
            distances.append(var)
        distances.sort()
        res = []
        for i in range(k):
            res.append(points[distances[i][1]])
        return res