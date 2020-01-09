# 제출 코드 - Runtime 95.96 Memory 73.68
class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = str(num)

        map = {"9": "6", "6": "9"}

        max = num
        for i in range(len(num_str)):
            tmp = num_str[:i] + map[num_str[i]] + num_str[i + 1:]
            tmp_int = int(tmp)
            if tmp_int > max:
                max = tmp_int

        return max


n1 = 9669
n2 = 9996
n3 = 9999

sol = Solution()
print(sol.maximum69Number(n1))
print(sol.maximum69Number(n2))
print(sol.maximum69Number(n3))
