#Problem Statement available at: https://leetcode.com/problems/palindrome-number/solution/
#Without converting to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0 or (x%10 == 0 and x!=0)):
            return False
        
        rev=0
        while(rev < x):
            rev = rev*10+ x%10
            x = x//10
                
        if(rev==x or rev//10 == x): #Since Middle digit doesn't matter in palindrome we can get rid of it by rev//10 Eg. 12321 x= 12 rev=123 so we can ignore 3
            return True
        else:
            return False