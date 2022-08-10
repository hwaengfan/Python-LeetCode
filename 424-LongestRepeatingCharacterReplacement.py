# O(26 * n) -> O(n) time -> 26 because max size of freq is 26 characters and we need
# to loop through to find max freq

def characterReplacement(s, k):
    freq = {}
    res = 0

    l = 0
    for r in range(len(s)):
        freq[s[r]] = 1 + freq.get(s[r], 0)
        if (r - l + 1) - max(freq.values()) > k:
            freq[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)

    return res
