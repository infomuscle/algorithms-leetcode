# 제출 코드 - Runtime 94.6 Memory 49.75
class Solution:
    def numberOfBeams(self, bank):
        beams = 0
        current, next = 0, 1
        while next <= len(bank) - 1:
            a = bank[current].count("1")
            b = bank[next].count("1")
            if a > 0 and b > 0:
                beams += a * b
                current = next
                next = current + 1
            else:
                if a > 0 and b == 0:
                    next += 1
                else:
                    current = next
                    next = current + 1

        return beams
