class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        for s in s1:
            freq1[s] = 1 + freq1.get(s, 0)

        freq2 = {}
        l = 0
        for r in range(len(s2)):
            freq2[s2[r]] = 1 + freq2.get(s2[r], 0)

            if r - l + 1 != len(s1):
                continue

            if freq1 == freq2:
                return True
            else:
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    freq2.pop(s2[l])
                l += 1
        return False
