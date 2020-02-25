#PS: https://leetcode.com/problems/plus-one/submissions/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rev_digits = digits[::-1] 
        carry = 1
        lst = []
        for d in rev_digits:
            if(d+carry > 9):
                lst.append(0)   
            else:
                lst.append(d+carry)
                carry = 0
        if carry == 1:
            lst.append(1)
            
        return lst[::-1]