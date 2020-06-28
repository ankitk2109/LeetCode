class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result, map_ = [], {}
        stack = ["JFK"]

        for i in tickets:
            if i[0] in map_:
                map_[i[0]].append(i[1])
            else:
                map_[i[0]] = [i[1]]
        
        for i in map_:
            map_[i].sort()

        while(stack):
            curr = stack[-1]
            if curr in map_ and len(map_[curr]) > 0:
                stack.append(map_[curr].pop(0))
            else:
                result.append(stack.pop())
        
        return result[::-1]