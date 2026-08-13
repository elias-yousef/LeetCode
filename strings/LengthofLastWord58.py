# Runtime 0ms beats 100%
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        leng = len(s) - 1
        count = 0
        if " " not in s:
            return len(s)
        while leng > 0:
            if s[leng] != " ":
                count += 1
            else:
                return count
            leng -= 1