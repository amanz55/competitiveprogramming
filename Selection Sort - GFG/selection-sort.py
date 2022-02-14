#User function Template for python3

class Solution: 
    def select(self, arr, i):
        selected = i
        for index in range(i, len(arr)):
            if arr[index] < arr[selected]:
                selected = index
        return selected
    
    def selectionSort(self, arr,n):
        #code here
        for index in range(n):
            sort = self.select(arr, index)
            if sort != index:
                arr[index], arr[sort] = arr[sort], arr[index]
    # def select(self, arr, i):
    #     arr1 = self.arr[i:]
    #     return min(arr1)
    
    # def selectionSort(self, arr,n):
    #     # self.arr=arr
    #     # for i in range(len(arr)-1):
    #     #     mymin = self.select(arr, i)
    #     #     myindex = self.arr.index(mymin)
    #     #     if myindex != i:
    #     #         self.arr[i], self.arr[myindex] = self.arr[myindex], self.arr[i]
    #     for index in range(n):
    #         self.arr=arr
    #         sort = self.select(arr, index)
    #         myindex = self.arr.index(sort)
    #         if myindex != index:
    #             self.arr[index], self.arr[myindex] = self.arr[myindex], self.arr[index]
    #     return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends