# Beats 85%

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for ch in ransomNote:
            if ch in counter:
                if counter[ch] == 0:
                    return False
                else:
                    counter[ch] -= 1
            if ch not in counter:
                return False
        return True