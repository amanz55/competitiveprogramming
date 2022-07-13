class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
                continue
            elif i % 3 == 0:
                ans.append("Fizz")
                continue
            elif i % 5 == 0:
                ans.append("Buzz")
                continue
            else:
                ans.append(str(i))
                continue
        return ans
        