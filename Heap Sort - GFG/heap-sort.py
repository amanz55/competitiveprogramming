#User function Template for python3

class Solution:
    def left_child(self,arr, n, i):
        return 2*i + 1
        
    def right_child(self,arr, n, i):
        return 2*i + 2
        
    def parent(self,arr, n, i):
        return (i - 1) // 2
        
    def insert(self,arr, n, val):
        arr.append(val)
        self.heapifyUp(arr, n, n)
        
    def remove(self, arr, n , i):
        n = len(arr)
        if n == 1:
            arr.pop()
        else:
            self.swap(i, n - 1, arr)
            arr.pop()
            self.heapifyDown(arr,0)
    
    def swap(self, i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]
        
    def modify(self, arr, n, i, val):
        arr[i] = val
        self.heapify(arr, n, i)
        
    def getmin(self, arr, n):
        n = len(arr)
        returned = arr[0]
        self.remove(arr, n, 0)
        return returned
        
    #Heapify function to maintain heap property.
    def heapifyUp(self,arr, n, i):
        n = len(arr)
        parent = self.parent(arr, n , i)
        if arr[i] < arr[parent]:
            while parent > -1:
                if arr[i] < arr[parent]:
                    self.swap(i, parent, arr)
                else:
                    break
                
                i = parent
                parent = self.parent(arr, n, i)
        else:
            return
        
    # def heapifyDown(self, arr):
    #     n = len(arr)
    #     i = 0
    #     while self.right_child(arr, n, i) < n:
    #         leftchild = self.left_child(arr, n, i)
    #         rightchild = self.right_child(arr, n, i)
            
    #         if rightchild < n:
    #             if arr[i] > arr[rightchild] and arr[i] > arr[leftchild]:
    #                 if rightchild > leftchild:
    #                     self.swap(i, leftchild, arr)
    #                     i = leftchild
    #                 else:
    #                     self.swap(i, rightchild, arr)
    #                     i = rightchild
    #             elif arr[i] > arr[rightchild]:
    #                 self.swap(i, rightchild, arr)
    #                 i = rightchild
    #             elif arr[i] > arr[leftchild]:
    #                 self.swap(i, rightchild, arr)
    #                 i = leftchild
    #         elif leftchild < n:
    #             if arr[i] > arr[leftchild]:
    #                 self.swap(i, leftchild, arr)
    #                 break
    #         else:
    #             break
    
    def heapifyDown(self,arr,i):
        right = self.right_child(arr,0,i)
        left = self.left_child(arr,0,i)
        
        minimum = i
        n = len(arr)
        if left < n and arr[left] < arr[minimum]:
            minimum = left
        if right < n and arr[right] < arr[minimum]:
            minimum = right
        
        if minimum != i:
            self.swap(minimum, i, arr)
            self.heapifyDown(arr, minimum)
            
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        self.arr2 = []
        # self.arr3 = [4,3,9,7]
        for i in range(len(arr)):
            self.insert(self.arr2, len(self.arr2), arr[i])
        # print(self.arr2)
        
        for i in range(len(arr)):
            arr[i] = self.getmin(self.arr2, n)
        # print(arr)
 
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends