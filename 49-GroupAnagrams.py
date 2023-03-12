class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)

        for word in strs:
            arr = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                arr[idx] += 1
            hashmap[tuple(arr)].append(word)

        return hashmap.values()
