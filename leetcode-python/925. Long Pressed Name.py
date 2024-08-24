# 제출 코드 - Runtime 91.86 Memory 100
class Solution:
    def isLongPressedName(self, name, typed):
        nameSplit = self.chrSpliter(name)
        typedSplit = self.chrSpliter(typed)

        if (len(nameSplit) != len(typedSplit)):
            return False

        for i in range(len(nameSplit)):
            if nameSplit[i][0] != typedSplit[i][0] or len(nameSplit[i]) > len(typedSplit[i]):
                return False
        return True

    def chrSpliter(self, chr):
        chrList = []
        temp = ""
        for i in range(len(chr)):
            temp += chr[i]

            if i == len(chr) - 1 or chr[i] != chr[i + 1]:
                chrList.append(temp)
                temp = ""
        return chrList

sample1 = ["alex", "aaleex"]
sample2 = ["saeed", "ssaaedd"]
sample3 = ["leelee", "lleeelee"]
sample4 = ["laiden", "laiden"]
sample5 = ["pyplrz", "ppyypllr"]

sol = Solution()
print(sol.isLongPressedName(sample1[0], sample1[1]))
print(sol.isLongPressedName(sample2[0], sample2[1]))
print(sol.isLongPressedName(sample3[0], sample3[1]))
print(sol.isLongPressedName(sample4[0], sample4[1]))
print(sol.isLongPressedName(sample5[0], sample5[1]))