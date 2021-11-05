import time


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        l, r = 0, 1

        biggest = ""
        while True:
            if l + len(biggest) >= len(s):
                break

            front = s[l:r]
            reversed_front = front[::-1]
            rear1 = s[r + 1: r + 1 + r - l]
            rear2 = s[r:r + r - l]
            # print(l, r)
            # print(s, front, rear1, rear2)

            if rear1 == reversed_front:
                substr = front + s[r] + reversed_front
                biggest = max(biggest, substr, key=len)
            elif rear2 == reversed_front:
                substr = front + reversed_front
                biggest = max(biggest, substr, key=len)

            if r - l >= len(s) // 2:
                r = l + len(biggest) - 1
                l += 1
                continue

            r += 1

        return biggest


sol = Solution()

s1 = "babad"
s2 = "cbbd"
s3 = "a"
s4 = "ac"
s5 = "wsgdzojcrxtfqcfkhhcuxxnbwtxzkkeunmpdsqfvgfjhusholnwrhmzexhfqppatkexuzdllrbaxygmovqwfvmmbvuuctcwxhrmepxmnxlxdkyzfsqypuroxdczuilbjypnirljxfgpuhhgusflhalorkcvqfknnkqyprxlwmakqszsdqnfovptsgbppvejvukbxaybccxzeqcjhmnexlaafmycwopxntuisxcitxdbarsicvwrvjmxsapmhbbnuivzhkgcrshokkioagwidhmfzjwwywastecjsolxmhfnmgommkoimiwlgwxxdsxhuwwjhpxxgmeuzhdzmuqhmhnfwwokgvwsznfcoxbferdonrexzanpymxtfojodcfydedlxmxeffhwjeegqnagoqlwwdctbqnuxngrgovrjesrkjrfjawknbrsfywljscfvnjhczhyeoyzrtbkvvfvofykkwoiclgxyaddhpdoztdhcbauaagjmfzkkdqexkczfsztckdlujgqzjyuittnudpldjvsbwbzcsazjpxrwfafievenvuetzcxynnmskoytgznvqdlkhaowjtetveahpjguiowkiuvikwewmgxhgfjuzkgrkqhmxxavbriftadtogmhlatczusxkktcsyrnwjbeshifzbykqibghmmvecwwtwdcscikyzyiqlgwzycptlxiwfaigyhrlgtjocvajcnqyenxrnjgogeqtvkxllxpuoxargzgcsfwavwbnktchwjebvwwhfghqkcjhuhuqwcdsixrkfjxuzvhjxlyoxswdlwfytgbtqbeimzzogzrlovcdpseoafuxfmrhdswwictsctawjanvoafvzqanvhaohgndbsxlzuymvfflyswnkvpsvqezekeidadatsymbvgwobdrixisknqpehddjrsntkqpsfxictqbnedjmsveurvrtvpvzbengdijkfcogpcrvwyf"
s6 = "bb"
s7 = "abb"
s8 = "ccc"

print(sol.longestPalindrome(s1))
print(sol.longestPalindrome(s2))
print(sol.longestPalindrome(s3))
print(sol.longestPalindrome(s4))

start = time.time()
print(sol.longestPalindrome(s5))
print(time.time() - start)

print(sol.longestPalindrome(s6))
print(sol.longestPalindrome(s7))
print(sol.longestPalindrome(s8))
