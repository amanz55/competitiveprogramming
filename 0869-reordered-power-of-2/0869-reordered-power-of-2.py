class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count_one = Counter(str(n))
        for i in range(32):
            number = 1 << i
            count_two = Counter(str(number))
            if count_one == count_two:
                return True
        return False
            
        