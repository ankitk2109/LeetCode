PS: https://leetcode.com/problems/pascals-triangle/submissions/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        
        if numRows == 1:
            return [[1]]
        
        for i in range(1,numRows+1):
            
            cur_row = [1]*i #initializing all the values with 1
            
            for j in range(1,i-1): #Will exclude 1st and last index of previous resultant row
                cur_row[j] = res[i-2][j-1] + res[i-2][j]
            
            res.append(cur_row)
        
        return res
        
            