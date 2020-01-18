class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        len_num = len(nums)
        lst = []
        for i in range(0,len_num,2):
            lst += [nums[i+1]] * nums[i]
        return lst