class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        sort = [[] for i in range(len(nums) + 1)]
        repeat = {}

        for num in nums:
            repeat[num] = 1 + repeat.get(num, 0)

        for num, count in repeat.items():
            sort[count].append(num)

        for i in range(len(sort) - 1, -1, -1):
            for num in sort[i]:
                res.append(num)
                if len(res) == k:
                    return res
