class Solution: 
    def select(self, arr, i):
        arr1 = arr[i:]
        return arr1.index(min(arr1)) + i
    
    def selectionSort(self, arr,n):
        for i in range(n):
            minindex = self.select(arr, i)
            if minindex != i:
                arr[i], arr[minindex] = arr[minindex], arr[i]
