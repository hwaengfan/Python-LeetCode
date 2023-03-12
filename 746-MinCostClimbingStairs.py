class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            c1 = cost[i] + cost[i + 1]
            c2 = cost[i] + cost[i + 2]
            cost[i] = min(c1, c2)
        return min(cost[0], cost[1])
