def climbStairs(n):
    n1, n2 = 1, 1

    for i in range(n - 1):
        temp = n1
        n1 = n1 + n2
        n2 = temp

    return n1
