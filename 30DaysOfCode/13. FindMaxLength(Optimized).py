class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return 0
        global_max = 0
        count = 0
        dic = {0:-1} #key: running count, value: index of current count(default value is kept -1 intentionally)
        for idx, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in dic:
                global_max = max(global_max, idx - dic[count])
            else:
                dic[count] = idx
        return global_max