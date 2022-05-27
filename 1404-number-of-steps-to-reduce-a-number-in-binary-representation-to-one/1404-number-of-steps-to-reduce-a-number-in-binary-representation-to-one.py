class Solution:
    def numSteps(self, s: str) -> int:
        target = int(s, 2)
        count = 0
        while target > 1:
            print(target)
            if target % 2 == 0:
                target = target // 2
            else:
                target += 1
            count += 1
        return count