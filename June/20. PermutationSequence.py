class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        fact = factorial(n)
        place = k
        digits = list(range(1, n+1))
        for i in range(n, 0, -1):
            fact = fact / i
            index = ceil(place / fact) - 1
            digit = digits[index]
            del digits[index]

            res.append(str(digit))
            place = k % fact
            if place == 0:
                place = fact
        return ''.join(res)