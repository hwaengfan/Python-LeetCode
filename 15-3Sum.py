class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            # eliminate duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - num

            # find two numbes add up to target
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    # eliminate duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
        return res
