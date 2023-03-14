class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.checkPalindrome(s, l + 1, r) or self.checkPalindrome(s, l, r - 1)
            else:
                l += 1
                r -= 1
        return True

    def checkPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
