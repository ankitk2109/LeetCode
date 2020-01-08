#Problem Statement available at:https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while( i < len(nums)-1):
            if(nums[i] == nums[i+1]):
                nums.pop(i)
            else:
                i = i+1
                
        return(len(nums))