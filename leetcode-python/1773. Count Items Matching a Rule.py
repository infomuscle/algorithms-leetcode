# 제출 코드 - Runtime 100 Memory 50
class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        keys = {"type": 0, "color": 1, "name": 2}
        return len([item for item in items if item[keys[ruleKey]] == ruleValue])


i1 = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
rk1 = "color"
rv1 = "silver"

sol = Solution()

print(sol.countMatches(i1, rk1, rv1))
