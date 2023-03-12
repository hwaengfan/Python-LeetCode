class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seen = set(nums)

        for num in nums:
            if num - 1 not in seen:
                length = 1
                while num + length in seen:
                    length += 1
                res = max(res, length)

        return res
