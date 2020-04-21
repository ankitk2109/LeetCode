class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        if all(i<0 for i in nums):#if all elements are less than zero
            return max(nums)
        
        global_max= 0        
        local_max = 0
        for num in nums:
            local_max += num
            
            if(local_max)<0:
                local_max = 0
                
            elif(local_max>global_max):
                global_max = local_max
                
        return(global_max)