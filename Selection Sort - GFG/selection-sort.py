#User function Template for python3

class Solution: 
    def select(self, arr, i):
        arr1 = arr[i:]
        return arr1.index(min(arr1)) + i
    
    def selectionSort(self, arr,n):
        for i in range(n):
            minindex = self.select(arr, i)
            if minindex != i:
                arr[i], arr[minindex] = arr[minindex], arr[i]

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