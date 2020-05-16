class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while(len(stones)>1):
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            if x == y:
                if len(stones) == 0: #If x and y are the last elements.
                    return 0
                else:
                    pass
            else:
                y = y-x
                stones.append(y)
                
        return stones[0]