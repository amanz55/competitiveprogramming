#5min
arr=[0,2,0,5,0,1,8,3,0,6,4,0,7]
def moveZeros(arr):
  for i in arr:
    if i==0:
      arr.remove(i)
      arr.append(i)
moveZeros(arr)      
print(arr)
