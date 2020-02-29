class Solution:
    def maxArea(self, height: List[int]) -> int:
        def container(start, end, start_h, end_h):
            waterQty = (end-start) * min(start_h,end_h)
            return waterQty
        
        lst = []
        for i in range (len(height)-1):
            for j in range (i+1,len(height)):
                lst.append(container(i, j, height[i], height[j]))
                
        return (max(lst))
