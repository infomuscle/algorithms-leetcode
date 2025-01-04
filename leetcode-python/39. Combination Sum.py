# 제출 코드 - Runtime 8.85 Memory 6.54
class Solution:
    def combinationSum(self, candidates, target):
        result = set()

        handled = set()
        combinations = [tuple([candidate]) for candidate in candidates]
        while combinations:
            combination = combinations.pop()
            handled.add(combination)
            sum_combination = sum(combination)
            if sum_combination == target:
                result.add(tuple(combination))
                continue
            if sum_combination < target:
                new_combinations = filter(lambda x: x not in handled, [tuple(sorted(combination + tuple([candidate]))) for candidate in candidates])
                combinations.extend(list(new_combinations))

        return list(result)


sol = Solution()

c1, t1 = [2, 3, 6, 7], 7
c2, t2 = [2, 3, 5], 8
c3, t3 = [2], 1

print(sol.combinationSum(c1, t1))
print(sol.combinationSum(c2, t2))
print(sol.combinationSum(c3, t3))
