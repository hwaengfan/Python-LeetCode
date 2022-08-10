def longestConsecutive(nums):
    hashset = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in hashset:
            length = 0
            while num + length in hashset:
                length += 1
            longest = max(longest, length)

    return longest
