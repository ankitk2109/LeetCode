class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_water_qty = 0
        while(i < j):
            max_water_qty = max(max_water_qty,min(height[i], height[j])*(j-i))
            
            #We need to find two points. Hence we will keep on incrementing i in forward direction and decrementing j in backward direction untill i < j.
            
            if(height[i] < height[j]):
                i += 1
            
            else:
                j -= 1
            
        return(max_water_qty)
                
            