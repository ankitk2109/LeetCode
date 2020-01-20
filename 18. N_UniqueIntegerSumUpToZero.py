#Problem Statement Available at: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero

class Solution:
    def sumZero(self, n: int) -> List[int]:
        lst=[]
        if n==1:
            return [0]
        elif(n%2 != 0):
            lst.append(0)
            for i in range(1,n):
                lst.append(i)
                lst.append(-i)
                if(len(lst) == n):
                    break
        else:
            for i in range(1,n):
                lst.append(i)
                lst.append(-i)
                if(len(lst) == n):
                    break
                
        #print(lst)
        return lst
            