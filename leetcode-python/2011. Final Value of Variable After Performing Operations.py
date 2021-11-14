# 제출 코드 - Runtime 96.94 Memory 48.37
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ops = {"++X": 1, "X++": 1, "--X": -1, "X--": -1}
        return sum(map(lambda o: ops.get(o), operations))


o1 = ["--X", "X++", "X++"]
o2 = ["++X", "++X", "X++"]
o3 = ["X++", "++X", "--X", "X--"]

sol = Solution()

print(sol.finalValueAfterOperations(o1))
print(sol.finalValueAfterOperations(o2))
print(sol.finalValueAfterOperations(o3))
