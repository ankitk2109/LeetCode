#Problem Statement available at: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        #mat = []
        total_odd = 0
        mat = [[0 for _ in range(m)] for _ in range(n)]

        for j in indices:
            r = j[0]
            c = j[1]
            for e in range(len(mat[r])):
                mat[r][e] = mat[r][e] + 1

            for k in range(n):
                mat[k][c] = mat[k][c] + 1

        for i in range(n):
            for j in range(m):
                if mat[i][j] %2 != 0:
                    total_odd = total_odd +1

        return total_odd