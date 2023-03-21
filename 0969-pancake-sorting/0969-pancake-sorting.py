class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []
        length = len(arr)
        
        for i in range(length - 1, -1, -1):
            maximum = max(arr[:i + 1])
            if maximum == arr[i]:
                continue
            index = arr.index(maximum)
            temp = arr[:index + 1][::-1] + arr[index + 1:i + 1]
            arr = temp[::-1] + arr[i + 1:]            
            answer.append(index + 1)
            answer.append(i + 1)
            
        return answer