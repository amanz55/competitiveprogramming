class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        temp=[]
        arr3=arr2.copy()
        for i in arr1:
            if i in arr2:
                for j in range(len(arr2)):
                    if arr2[j]==i:
                        if j==0:
                            arr2.insert(1,i)
                            break
                        else:
                            arr2.insert(j,i)
                            break
            else:
                temp.append(i)
        temp.sort()
        arr2.extend(temp)
        for ele in arr3:
            arr2.remove(ele)
        return arr2
        
