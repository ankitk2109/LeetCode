class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==0 or n==1:
            return n
        total = 0
        for i in range(1,n+1):
            if (total+i) <= n:
                total += i
            else:
                return (i-1)