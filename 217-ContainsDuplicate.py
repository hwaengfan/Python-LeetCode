def containsDuplicate(nums):
    map = set()
    for num in nums:
        if num in map:
            return True
        else:
            map.add(num)
    return False
