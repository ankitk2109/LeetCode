class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c = collections.Counter(S)
        count = 0
        for jewel in J:
            count += c[jewel]
        
        return count