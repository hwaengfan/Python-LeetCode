class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            currLevel = []
            for j in range(len(res[-1]) + 1):
                currLevel.append(temp[j] + temp[j + 1])
            res.append(currLevel)
        return res
