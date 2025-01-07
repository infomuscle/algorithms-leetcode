# 제출 코드 - Runtime 32.92 Memory 5.12
class Solution:
    def merge(self, intervals):

        intervals.sort(key=lambda x: (x[0], x[1]))

        result = []
        temp = []
        for i in range(len(intervals)):
            if len(temp) == 0:
                temp.extend(intervals[i])
                continue
            start, end = intervals[i][0], intervals[i][1]
            if start <= temp[1]:
                temp_end = temp.pop()
                temp.append(max(end, temp_end))
            else:
                result.append(temp)
                temp = []
                temp.extend(intervals[i])

        if len(temp) > 0:
            result.append(temp)

        return result


sol = Solution()

i1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
i2 = [[1, 4], [4, 5]]
i3 = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]

print(sol.merge(i1))
print(sol.merge(i2))
print(sol.merge(i3))
