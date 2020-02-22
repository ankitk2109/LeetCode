#PS: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s):
            global_len = 1
            for i in range(len(s)-1):
                max_sub_str = []
                max_sub_str.append(s[i])
                local_len = 1
                for j in range(i+1,len(s)):
                    if s[j] not in max_sub_str:
                        max_sub_str.append(s[j])
                        local_len += 1
                        if(global_len < local_len):
                            global_len = local_len

                    else:
                        break
            return(global_len)
        else:
            return 0