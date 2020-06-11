class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left = 0
        right = len(nums)
        mid = (left + right)//2 
        while(left < right):
                       
            if nums[mid] == target:
                return mid
            
            if(target < nums[mid]):
                right = mid
            
            if(target > nums[mid]):
                left = mid+1
            mid = (left + right)//2 
                
        return mid