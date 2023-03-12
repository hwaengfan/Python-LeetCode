class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res = (num - 3) // 3

        if 3 * res + 3 == num:
            return [res, res + 1, res + 2]
        else:
            return []
