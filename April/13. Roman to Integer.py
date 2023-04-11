class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        answer = 0
        roma = {
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1,

        }
        for i in range(length - 1):
            if roma[s[i+1]] > roma[s[i]]:
                answer = answer - roma[s[i]]
            else:
                answer = answer + roma[s[i]]
        answer = answer + roma[s[length - 1]]
        return answer
        
