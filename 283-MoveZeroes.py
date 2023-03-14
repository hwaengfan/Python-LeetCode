class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for _ in range(len(nums)):
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
            else:
                idx += 1
