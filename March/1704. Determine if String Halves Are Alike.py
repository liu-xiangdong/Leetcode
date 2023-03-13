class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = int(len(s) / 2)
        right = s[0:a]
        left = s[a:]
        num1 = num2 = 0
        for i in right:
            if i in "aeiouAEIOU":
                num1 = num1+1
        for j in left:
            if j in "aeiouAEIOU":
                num2 = num2+1
        return num1 == num2
  
'''
method 2
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s.lower()
        b = len(a)
        c = a[0:int(b/2)]
        d = a[int(b/2):]
        if c.count('a')+c.count('e')+c.count('i')+c.count('o')+c.count('u') == d.count('a')+d.count('e')+d.count('i')+d.count('o')+d.count('u'):
            return True
        else:
            return False
'''
