import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[]
        len_ = len(nums)
        l=[1] * len_
        r=[1] * len_
        
        for i in range(1,len_):
            l[i] = l[i-1] * nums[i-1]
        
        for j in range(len_-2, -1,-1):
            r[j] = r[j+1] * nums[j+1]

        for k in range(len_):
            out.append(l[k] * r[k])
    
        return(out)