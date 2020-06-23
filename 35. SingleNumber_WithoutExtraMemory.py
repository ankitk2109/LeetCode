class Solution:
    def singleNumber(self, nums: List[int]) -> int: 

        ans = (sum(list(set(nums)))*3-sum(nums))//2
        return ans