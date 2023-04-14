class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        s_last = s[-1]
        s_last_list = list(s_last)
        a = len(s_last_list)
        return(a)
