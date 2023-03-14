class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for c in s[::-1]:
            if c == " ":
                if length >= 1:
                    return length
            else:
                length += 1
        return length
