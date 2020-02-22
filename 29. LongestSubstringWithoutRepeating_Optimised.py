#PS: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        end = 0
        max_len = 0
        '''
        Logic is create a window between start and end until the end is less than len(string)
        Add the element into seen dict if not present. If the element is present start 
        removing element from start becuase we want a continuous longest substring
        '''
        while(end<len(s)):
            if s[end] not in seen:
                seen[s[end]] = True
                end += 1
                max_len = max(len(seen), max_len)
            else:
                del seen[s[start]]
                start += 1
                
        return max_len