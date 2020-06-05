class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_costs = sorted(costs,key = lambda x:x[0]-x[1])
        print(sorted_costs)
        total_min_cost = 0 
        for i in range(len(costs)):
            if i < len(costs) / 2:
                total_min_cost += sorted_costs[i][0]
            else:
                total_min_cost += sorted_costs[i][1]
        return total_min_cost