#Problem Statement at: https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != val : #if current element is not val then assign it to first index of nums and increment i(this would be the length eventually)
                nums[i] = nums[j]  
                i+=1
        return i