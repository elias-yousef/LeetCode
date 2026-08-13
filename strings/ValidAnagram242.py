# 15ms beats 44% because sorted() use Nlog(N) complexity
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)