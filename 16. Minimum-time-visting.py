#Problem Statement available at: https://leetcode.com/problems/minimum-time-visiting-all-points

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        len_points = len(points)
        time = 0
        #print(len_points)
        for i in range(len_points-1):
            time += max(abs(points[i][0] - points[i+1][0]), abs(points[i][1] - points[i+1][1]))
            '''
            fp = points[i]
            sp = points[i+1]
            t1 = abs(sp[0] - fp[0])
            t2 = abs(sp[1] - fp[1])
            time += max(t1,t2)
            '''
        return time