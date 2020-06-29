class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            nums = start + 2*i
            if i == 0:
                result = start
            else:
                result = result^nums
        return(result)