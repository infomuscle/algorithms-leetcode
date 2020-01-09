# 제출 코드 - Runtime 52.17 Memory 39.51
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains):
        counts = defaultdict(int)
        for cpdomain in cpdomains:
            time, domain = cpdomain.split(" ")
            fragments = domain.split(".")
            for i in range(len(fragments)):
                subdomain = ".".join(fragments[i:])
                counts[subdomain] += int(time)

        return ["%s %s" % (counts[key], key) for key in counts]
