# 제출 코드 - Runtime 41.37 Memory 98.33
class Solution:
    def summaryRanges(self, nums):
        result = []

        temp = []
        for i, num in enumerate(nums):
            if len(temp) == 0 or num == temp[-1] + 1:
                temp.append(num)
                continue
            result.append("{0}".format(temp[0]) if len(temp) == 1 else "{0}->{1}".format(temp[0], temp[-1]))
            temp = [num]

        if len(temp) != 0:
            result.append("{0}".format(temp[0]) if len(temp) == 1 else "{0}->{1}".format(temp[0], temp[-1]))

        return result
