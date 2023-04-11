class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        n = len(arr)
        difference = list()
        for i in range(n - 1):
            a = arr[i + 1] - arr[i]
            difference.append(a)
        ans = list()
        b = min(difference)
        for i in range(n - 1):
            if difference[i] == b:
                ans.append([arr[i], arr[i + 1]])
        return ans
