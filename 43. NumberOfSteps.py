class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num < 2:
            return num
        else:
            steps = 0
            while num:
                num, rem = divmod(num, 2)
                steps = steps + 1 + rem
            return steps-1