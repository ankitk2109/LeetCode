class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquare(n):
            digits = [int(i) for i in (str(n))]
            for i in range(len(digits)):
                digits[i] = digits[i]**2
            #print(sum(digits))
            return sum(digits)
        
        while True:
            n = sumOfSquare(n)
            if n == 1:
                return True
            elif n==4: #Seeing the pattern it can be seen that digit "4" repeats in every cycle if sum doesn't add up to 1.  
                return False