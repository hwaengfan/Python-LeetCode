class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n) time and O(n) space
        remain = {}
        for i in range(len(numbers)):
            if numbers[i] in remain:
                return [remain[numbers[i]] + 1, i + 1]
            else:
                remain[target - numbers[i]] = i

        # O(n) time and O(1) space
        l, r = 0, len(numbers) - 1
        while(l < r):
            currSum = numbers[l] + numbers[r]
            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
