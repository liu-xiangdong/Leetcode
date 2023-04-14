class Solution:
    def plusOne(self, digits):
        num = ""
        for i in digits:
            num = num + str(i)
        num = int(num)
        num = num + 1
        num = str(num)
        ans = []
        for j in num:
            ans.append(int(j))
        return(ans)
