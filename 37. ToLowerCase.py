class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.translate({k:k+32 for k in range(65,65+26)})
        