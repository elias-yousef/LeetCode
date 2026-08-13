# Runtime beats 17%
# memory beats 76%

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        text = ""
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                text += ch
        length = len(text) - 1
        i = 0
        while length > i:
            if text[length] != text[i]:
                return False
            length -= 1
            i += 1
        return True