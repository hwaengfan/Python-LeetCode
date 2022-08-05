# O(n) time | O(n) space

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sSeen, tSeen = {}, {}

        for c in s:
            sSeen[c] = sSeen.get(c, 0) + 1

        for c in t:
            tSeen[c] = tSeen.get(c, 0) + 1

        return sSeen == tSeen
