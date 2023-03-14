class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replaceS = {}
        replaceT = {}
        i = 0
        for i in range(len(s)):
            if (s[i] in replaceS and replaceS[s[i]] != t[i]) or (t[i] in replaceT and replaceT[t[i]] != s[i]):
                return False
            replaceS[s[i]] = t[i]
            replaceT[t[i]] = s[i]
        return True
