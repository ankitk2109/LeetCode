#PS: https://leetcode.com/problems/add-binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a and b:
            sum_ = int(a,2) + int(b,2)
            return (bin(sum_)[2:])
        elif(a or b):
            return(a if a else b)
        else:
            return '0'