#Problem Statement Available at: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero
class Solution:
    def sumZero(self, n: int) -> List[int]:
        lst=[]
        for i in range(0,n//2):
            lst.append(i+1)
            lst.append(-(i+1))
        if n%2:
            lst.append(0)
        return lst
        