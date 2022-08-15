def nextGreaterElements(nums):
    lnums = nums * 2
    stack = []
    res = [-1] * len(nums)

    for i, n in enumerate(lnums):
        while stack and n > stack[-1][0]:
            num, index = stack.pop()
            res[index] = n
        if i < len(nums):
            stack.append((n, i))

    return res
