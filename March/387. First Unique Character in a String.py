class Solution(object):
    def firstUniqChar(self, s: str) -> int:
        i = 0
        noUniqChar = ""  #如果每次循环的字母已经存在于noUniqChar字符串中，则跳过 如果不存在，则判断是否在往后的s字符串中存在，有就加到noUniqChar中，没有就可以return 结果。
        lens = len(s)
        while i < lens:
            ch = s[i]
            if ch in noUniqChar :
               i = i + 1
            else:
                if ch in s[i + 1:] :
                    noUniqChar= noUniqChar + ch
                    i = i + 1
                else:
                    return i
        return -1
"""
class Solution(object):
    def firstUniqChar(self, s: str) -> int:
        a = len(s)
        s = list(s)
        find = False
        i = 0
        while i < a and not find:
            b = s[i]
            s.remove(s[i])
            if b in s:
                pass
            else:
                return i
                find =True
            s.insert(i,b)
            i = i+1
        return -1
"""
