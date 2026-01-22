# 제출 코드 - Runtime 5.00 Memory 23.49
from collections import deque


class Solution:
    def accountsMerge(self, accounts):
        queue = deque(accounts)
        for i in range(len(queue)):
            target = queue.popleft()
            target_name, target_emails = target[0], set(target[1:])
            for j in range(len(queue)):
                next = queue.popleft()
                next_name, next_emails = next[0], set(next[1:])
                if target_name != next_name:
                    queue.append(next)
                    continue
                if len(target_emails.intersection(next_emails)) == 0:
                    queue.append(next)
                    continue
                target_emails = target_emails.union(next_emails)
            merged = [target_name]
            merged.extend(sorted(list(target_emails)))
            queue.append(merged)

        return list(queue)


sol = Solution()

a1 = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]

print(sol.accountsMerge(a1))
