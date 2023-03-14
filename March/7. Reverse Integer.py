class Solution:
    def reverse(self, x: int) -> int:
        if x < 10 and x > -10:
            return x
        else:
            x = str(x)
            a = len(x)
            if x[0] == "-":
                y = x[0]
                for i in range(1, a):
                    y = y + x[a - i]
            else:
                y = ""
                for j in range(a):
                    y = y + x[a - j - 1]
        y = int(y)
        #"012"经过int后为12
        if y < -2 ** 31 or y > 2 ** 31 - 1:
            return 0
        else:
            return y
