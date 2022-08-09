def twoSum(nums, target):
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [i, prevMap[diff]]
        prevMap[n] = i
