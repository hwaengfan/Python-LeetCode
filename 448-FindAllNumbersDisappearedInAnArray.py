class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)

        return res
