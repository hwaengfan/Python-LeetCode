from collections import defaultdict


def groupAnagrams(strs):
    hashmap = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            pos = ord(c) - ord('a')
            count[pos] += 1
        hashmap[tuple(count)].append(s)

    return hashmap.values()
