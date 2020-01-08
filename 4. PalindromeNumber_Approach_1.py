#Problem Statement available at: https://leetcode.com/problems/palindrome-number/solution/
#By converting no. to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        
        else:
            if(str(x) == str(x)[::-1]):
                return True
            else:
                return False