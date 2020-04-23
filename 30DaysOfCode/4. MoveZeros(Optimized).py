class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_idx = 0 
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[non_zero_idx]= nums[i]
                non_zero_idx += 1

        #appending zeros ahead of non zero indexes
        for j in range(non_zero_idx,len(nums)):
            nums[j] = 0
        