class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return 0
        global_max = 0
        for i in range(len(nums)-1):
            bin_dict = {0:0,1:0}
            local_max = 0
            bin_dict[nums[i]] += 1
            
            for j in range(i+1, len(nums)):
                bin_dict[nums[j]] += 1    
                
                if(bin_dict[0] == bin_dict[1]):
                    local_max = (j-i)+1
                    if(global_max<=local_max):
                        global_max = local_max
        return global_max
            