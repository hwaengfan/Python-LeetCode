def findMin(arr):
    l, r = 0, len(arr) - 1
    res = arr[0]

    while l <= r:
        if arr[l] < arr[r]:
            res = min(res, arr[l])
            break

        m = (l + r) // 2
        res = min(res, arr[m])

        if arr[m] >= arr[l]:
            l = m + 1
        else:
            r = m - 1

    return res
