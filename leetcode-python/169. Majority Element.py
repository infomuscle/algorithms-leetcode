# 제출 코드 - Runtime 88.52 Memory 49.21
class Solution:
    def majorityElement(self, nums) -> int:

        count = dict()
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        answer = 0
        max = 0
        for key in count:
            if count[key] > max:
                max = count[key]
                answer = key

        return answer


sol = Solution()

l1 = [3, 2, 3]
l2 = [2, 2, 1, 1, 1, 2, 2]

print(sol.majorityElement(l1))
print(sol.majorityElement(l2))
