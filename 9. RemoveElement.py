#Problem Statement at: https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if (len(nums)==0):
            return 0
        
        if val not in nums:
            return len(nums)
        
        count = 0
        
        for ele in nums:
            if ele == val:
                count+=1
        
        for i in range(count):
            nums.remove(val)
        
        return(len(nums))