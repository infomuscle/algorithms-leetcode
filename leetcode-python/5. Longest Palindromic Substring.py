import time


class Solution:
    def longestPalindrome(self, s: str) -> str:
        for len_of_substr in range(len(s), 1, -1):
            for start_idx in range(0, len(s) - len_of_substr + 1):
                substr = s[start_idx:start_idx + len_of_substr]
                if self.is_palindrome(substr):
                    return substr
        return s[0]

    def is_palindrome(self, s):
        len_of_str = len(s)
        half_idx = len_of_str // 2
        front = s[:half_idx]
        if len_of_str % 2 == 0:
            rear = s[half_idx:]
        else:
            rear = s[half_idx + 1:]

        return front == rear[::-1]


sol = Solution()

s1 = "babad"
s2 = "cbbd"
s3 = "a"
s4 = "ac"
s5 = "wsgdzojcrxtfqcfkhhcuxxnbwtxzkkeunmpdsqfvgfjhusholnwrhmzexhfqppatkexuzdllrbaxygmovqwfvmmbvuuctcwxhrmepxmnxlxdkyzfsqypuroxdczuilbjypnirljxfgpuhhgusflhalorkcvqfknnkqyprxlwmakqszsdqnfovptsgbppvejvukbxaybccxzeqcjhmnexlaafmycwopxntuisxcitxdbarsicvwrvjmxsapmhbbnuivzhkgcrshokkioagwidhmfzjwwywastecjsolxmhfnmgommkoimiwlgwxxdsxhuwwjhpxxgmeuzhdzmuqhmhnfwwokgvwsznfcoxbferdonrexzanpymxtfojodcfydedlxmxeffhwjeegqnagoqlwwdctbqnuxngrgovrjesrkjrfjawknbrsfywljscfvnjhczhyeoyzrtbkvvfvofykkwoiclgxyaddhpdoztdhcbauaagjmfzkkdqexkczfsztckdlujgqzjyuittnudpldjvsbwbzcsazjpxrwfafievenvuetzcxynnmskoytgznvqdlkhaowjtetveahpjguiowkiuvikwewmgxhgfjuzkgrkqhmxxavbriftadtogmhlatczusxkktcsyrnwjbeshifzbykqibghmmvecwwtwdcscikyzyiqlgwzycptlxiwfaigyhrlgtjocvajcnqyenxrnjgogeqtvkxllxpuoxargzgcsfwavwbnktchwjebvwwhfghqkcjhuhuqwcdsixrkfjxuzvhjxlyoxswdlwfytgbtqbeimzzogzrlovcdpseoafuxfmrhdswwictsctawjanvoafvzqanvhaohgndbsxlzuymvfflyswnkvpsvqezekeidadatsymbvgwobdrixisknqpehddjrsntkqpsfxictqbnedjmsveurvrtvpvzbengdijkfcogpcrvwyf"

print(sol.longestPalindrome(s1))
print(sol.longestPalindrome(s2))
print(sol.longestPalindrome(s3))
print(sol.longestPalindrome(s4))

start = time.time()
print(sol.longestPalindrome(s5))
print(time.time() - start)
