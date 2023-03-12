class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        maxlen = 1
        len1 = len(s)
        for i in range(len1):
            len2 = 1
            str = s[i]
            for j in range(i + 1, len1):
                if s[j] in str:
                    break
                else:
                    len2 = len2 + 1
                    str = str + s[j]
            if len2 > maxlen:
                maxlen = len2
        return maxlen
