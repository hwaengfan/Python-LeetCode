class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(arr[i], currMax)
            arr[i] = currMax
            currMax = newMax
        return arr
