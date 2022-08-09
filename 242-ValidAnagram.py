def isAnagram(s, t):
    sSeen, tSeen = {}, {}

    for c in s:
        sSeen[c] = sSeen.get(c, 0) + 1

    for c in t:
        tSeen[c] = tSeen.get(c, 0) + 1

    return sSeen == tSeen
