# 제출 코드 - Runtime 5.38 Memory 33.39
class Solution:
    def subsets(self, nums):
        result = []
        nums = set(nums)

        def generate_sets(subsets, nums_left, subset):
            subsets.append(subset)
            for n in nums_left:
                s = subset.union({n})
                if s not in result:
                    generate_sets(subsets, nums_left - subset, s)

        generate_sets(result, nums, set())

        return result


sol = Solution()

n1 = [1, 2, 3]
n2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 0]
print(sol.subsets(n1))
print(sol.subsets(n2))
