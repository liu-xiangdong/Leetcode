class Solution:
    def climbStairs(self, n: int) -> int:
        s = [1, 2]
        if n <= 2:
            return s[n - 1]
        while len(s) < n:
            s.append(s[-1] + s[-2])
        return s[-1]
