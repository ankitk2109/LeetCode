#Problem available at: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        nums = list(map(str,nums))
        for ele in nums:
            if len(ele)%2==0:
                count +=1
        return count