class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        a = len(s)
        check = a // 2
        match = True
        i = 0
        while i < check and match:
            right = a - 1 - i
            if s[i] == s[right]:
                match = True
            else:
                match = False
            i = i + 1
        return match
# return str(x) == str(x)[::-1]
