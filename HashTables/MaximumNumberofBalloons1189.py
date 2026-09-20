# Beats 65%q

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        count = 0
        while True:
            if counter["o"] > 1 and counter["l"] > 1 and counter["b"] > 0 and counter["a"] > 0 and counter["n"] > 0:
                count += 1
                counter["o"] -= 2
                counter["l"] -= 2
                counter["b"] -= 1
                counter["n"] -= 1
                counter["a"] -= 1
            else:
                return count
        