class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset = {}

        for i, n in enumerate(nums1):
            hashset[n] = i

        stack = []
        res = [-1] * len(nums1)
        for n in nums2:
            while stack and n > stack[-1]:
                val = stack.pop()
                res[hashset[val]] = n
            if n in hashset:
                stack.append(n)

        return res
