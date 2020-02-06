#PS: https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        days = [0] * len(T)
        stack =[]
        
        for idx,value in enumerate(T):    
            while stack and stack[-1][1] <  value:
                temp = stack.pop()
                days[temp[0]] = idx-temp[0]
            
            stack.append((idx,value))
        
        return(days)