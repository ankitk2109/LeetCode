#Problem available at: https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        
        def con_to_lst(x):
            num_str = str(x)
            num_lst = [num for num in num_str]
            return num_lst
        
        def con_to_num(res):
            return int("".join(res))
        
        if(x == 0):
            return 0
        
        else:
            if(x<0):
                x = x * -1
                num_lst = con_to_lst(x)
                rev_num_lst = num_lst[::-1]
                if(rev_num_lst[0]=='0'):
                    rev_num_lst = rev_num_lst[1:]
                res = con_to_num(rev_num_lst)
                res = res * -1
                if(res >= ((2**31)-1) or res <= -(2**31)):
                    return 0

            else:
                num_lst = con_to_lst(x)
                rev_num_lst = num_lst[::-1]
                if(rev_num_lst[0]=='0'):
                    rev_num_lst = rev_num_lst[1:]
                res = con_to_num(rev_num_lst)
                if(res >= ((2**31)-1) or res <= -(2**31)):
                    return 0         

            return(res)            