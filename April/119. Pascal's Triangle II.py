class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            a = []
            a.append([1])
            a.append([1, 1])
            for i in range(1, rowIndex):
                b = []
                for j in range(i + 2):
                    if j == 0:
                        b.append(1)
                    elif j == i + 1:
                        b.append(1)
                    else:
                        b.append(a[i][j - 1] + a[i][j])
                a.append(b)
            return a[rowIndex]
