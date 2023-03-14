class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charCount = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        balloonCount = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}

        for c in text:
            if c in charCount:
                charCount[c] += 1

        res = float("inf")
        for key in charCount:
            res = min(res, charCount[key] // balloonCount[key])

        return res
