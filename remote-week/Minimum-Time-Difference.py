class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        differences=[]
        for i in range(len(timePoints)):
            lis=timePoints[i].split(":")
            lis[0]=int(lis[0])
            lis[1]=int(lis[1])
            lis=lis[0]*60 + lis[1]
            timePoints[i]=lis
        differences.append(1440-timePoints[-1]+timePoints[0])
        for j in range(len(timePoints)-1):
            temp=timePoints[j+1]-timePoints[j]
            differences.append(temp)
        return min(differences)
        
