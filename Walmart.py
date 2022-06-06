# Given an array, find continuous array that has at most two type.
# for example: arr = [1, 1, 2, 2, 2, 2, 3, 2, 1]
# output: [1, 1, 2, 2, 2, 2] because this is the longest continuous array that has at most two types

# Algo:
# hashset to keep track of 2 current pairs, and i - start + 1 to keep track of len of 2 current pairs
# when reach a new num: loop backward to find last of the 2 current pair, remove it, then update new start

def twoTypes(nums):
    hashset = set()
    maxLen = 0
    start = 0

    for i, num in enumerate(nums):
        if len(hashset) < 2 or num in hashset:
            hashset.add(num)
            maxLen = max(maxLen, i - start + 1)
        else:
            last = nums[i - 1]
            for j in range(i - 1, 0, -1):
                if (last != nums[j]):
                    start = j + 1
                    hashset.remove(nums[j])
                    hashset.add(num)
                    break

    return maxLen


nums = [1, 1, 2, 2, 2, 2, 3, 2, 1]
print(twoTypes(nums))
