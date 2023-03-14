class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPtr = 0
        for c in t:
            if sPtr < len(s) and s[sPtr] == c:
                sPtr += 1
        return sPtr == len(s)
