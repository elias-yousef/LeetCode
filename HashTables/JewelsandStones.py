# Beats 100%

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        # Time: O(n + m)
        s = set(jewels)
        for ch in stones:
            if ch in s:
                counter += 1
        return counter