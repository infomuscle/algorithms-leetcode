# 제출 코드 - Runtime 95.48 Memory 7.28
class Solution:
    def uniqueMorseRepresentations(self, words):
        morses = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--",
                  "--.."]

        morse_map = {}
        for i, m in enumerate(morses):
            morse_map[chr(i + 97)] = m

        word_map = {}
        for word in words:
            morse = "".join([morse_map[w] for w in word])
            word_map[morse] = True

        return len(word_map)


w1 = ["gin", "zen", "gig", "msg"]

sol = Solution()
print(sol.uniqueMorseRepresentations(w1))
