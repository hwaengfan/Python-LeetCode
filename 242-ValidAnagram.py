# https://leetcode.com/problems/valid-anagram/
# O(n) time | O(n) space

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        schar = {}

        for c in s:
            if c in schar:
                schar[c] += 1
            else:
                schar[c] = 1

        for c in t:
            if c not in schar:
                return False
            else:
                schar[c] -= 1
                if schar[c] == 0:
                    schar.pop(c)

        if len(schar) == 0:
            return True

        return False
