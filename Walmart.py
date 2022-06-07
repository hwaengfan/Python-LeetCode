# Given an array, find continuous array that has at most two type.
# for example: arr = [1, 1, 2, 2, 2, 2, 3, 2, 1]
# output: [1, 1, 2, 2, 2, 2] because this is the longest continuous array that has at most two types

# Algo:
# hashset to keep track of 2 current pairs, start and end are indicies of subarray
# when reach a new num: remove last num of subarray, add new num and update start

# O(n) time | O(2) space?

def twoTypes(nums):
    hashset = set()
    maxLen = 0
    start = 0
    end = 0

    for i, num in enumerate(nums):
        if len(hashset) < 2 or num in hashset:
            end = i
            hashset.add(num)
            maxLen = max(maxLen, end - start + 1)
        else:
            hashset.remove(nums[start])
            start = end + 1
            hashset.add(num)

    return maxLen


nums = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# nums = [1, 1, 2, 2, 2, 2, 3, 2, 1]
# nums = [0, 1, 1]
# nums = [1, 1]
# nums = []

print(twoTypes(nums))
