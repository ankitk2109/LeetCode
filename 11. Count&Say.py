#Problem Statement available at: https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        if n==2:
            return '11'
        else:
            prev = '11'
            res = ''
            c = 1
            for i in range(3,n+1): #For number of records,Let say if we want 5th record the loop will run like 3,4 and 5. 
                res = ''
                c = 1
                prev = prev+'$' #If two charachters are same at end then condition  won't go into else hence we need to add extra element so that res var will get updated.
                for j in range(len(prev)-1): #for number len(prev)-1 to avoid array out of index
                    if(prev[j] == prev[j+1]):
                        c += 1
                    else:
                        res = res + str(c)
                        res = res + prev[j]
                        c = 1
                prev = res
        
            return res
                