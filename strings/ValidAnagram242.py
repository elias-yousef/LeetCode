# 15ms beats 44% because sorted() use Nlog(N) complexity

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# new solution i came up with faster than that i wrote first
# beats 91% O(n)
# using Hash table

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_t = Counter(t)
        counter_s = Counter(s)
        return counter_t == counter_s