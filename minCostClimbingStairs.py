def minCostClimbingStairs(cost):
    if len(cost)==1:
        return 0
    if len(cost) ==2:
        return min(cost)
    else:
        return min(cost[0]+minCostClimbingStairs(cost[1:]), cost[1]+minCostClimbingStairs(cost[2:]))

cost = [2, 5, 10,12, 20]
print(minCostClimbingStairs(cost))