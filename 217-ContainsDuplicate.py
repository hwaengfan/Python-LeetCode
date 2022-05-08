# O(n) time | O(n) space

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = set()
        for num in nums:
            if num in map:
                return True
            else:
                map.add(num)
        return False
