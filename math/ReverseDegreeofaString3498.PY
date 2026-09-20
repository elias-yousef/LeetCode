# Beats 97.65%

class Solution:
    def reverseDegree(self, s: str) -> int:
        index = 1
        final = 0
        fin = 0
        for ch in s:
            val = ord(ch.lower()) - ord('a') - 26
            final += (-val) * index
            index += 1
        return final