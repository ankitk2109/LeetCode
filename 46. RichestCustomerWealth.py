# problem available at: https://leetcode.com/problems/richest-customer-wealth/discuss/1097611/python-one-line-solution

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return(max([sum(i) for i in accounts]))