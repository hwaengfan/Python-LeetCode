class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        i = 0
        while i < size:
            if nums[i] == val:
                for j in range(i + 1, size):
                    nums[j - 1] = nums[j]
                size -= 1
            else:
                i += 1
        return size
