def maxArea(height):
    l, r = 0, len(height) - 1
    maxArea = 0

    while l < r:
        area = (r - l) * min(height[l], height[r])
        maxArea = max(maxArea, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return maxArea
