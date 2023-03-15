class Solution:
    def longestCommonPrefix(self, s):
        a = len(s)
        b = [0] * len(s)
        for i in range(a):
            b[i] = len(s[i])
        c = min(b)
        # 字符串数组中最短字符串元素的长度
        common = ""
        if a == 0:
            return common
        else:
            j = 0
            match = True
            while j < c and match:
                k = 1
                while k < a and match:
                    if s[k][j] == s[0][j]:
                        pass
                    else:
                        match = False
                    k = k + 1
                if match:
                    common = common + s[0][j]
                j = j + 1
        return common
