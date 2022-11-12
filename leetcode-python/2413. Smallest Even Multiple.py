# 제출 코드 - Runtime 67.1 Memory 50.77
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        num = n
        while num % 2 != 0:
            num += n

        return num
