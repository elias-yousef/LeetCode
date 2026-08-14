# Beats 100%

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        leng = len(t)
        if s == "":
            return True
        if len(s) >= len(t):
            if s == t:
                return True
            return False
        while i <= leng - 1 and j <= len(s) - 1:
            if s[j] == t[i]:
                j += 1
            i += 1
        if j < len(s):
            return False
        return True