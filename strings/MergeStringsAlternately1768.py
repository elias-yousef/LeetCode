# Beats 72% on runtime

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        lis = []
        lw1 = len(word1)
        lw2 = len(word2)
        tallest = max(word1, word2, key=len)
        while i < max(lw1, lw2):
            if i < min(lw1, lw2):
                lis.append(word1[i])
                lis.append(word2[i])
            else:
                lis.append(tallest[i])
            i += 1
        return "".join(lis)