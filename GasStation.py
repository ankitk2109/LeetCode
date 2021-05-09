Problem available at: https://leetcode.com/problems/gas-station/submissions/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        surplus = 0
        deficit = 0
        start_idx = 0
        for i in range(len(gas)):
            surplus = surplus + gas[i] - cost[i]
            
            if surplus < 0:
                start_idx = i+1
                deficit += surplus
                surplus = 0
                
                
        if surplus + deficit >= 0:
            return start_idx
        else:
            return -1