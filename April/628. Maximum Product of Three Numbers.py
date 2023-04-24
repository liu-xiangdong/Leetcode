class Solution:
    def maximumProduct(self, nums):
        #一个数组三个数组成的最大乘积只有两种构成情况，第一种三个最大的数，第二种是最大的数与两个最小的相乘（负负得正，两个最小数的乘积大于第二大和第三大数的乘积）
        max1 = -float("inf")  #最大值
        max2 = -float("inf")  #第二大
        max3 = -float("inf")  #第三大
        min0 = float("inf")  #最小
        min1 = float("inf")  #第二小
        for i in nums:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i

            if i < min0:
                min1 = min0
                min0 = i
            elif i < min1:
                min1 = i
        a = max(max1 * max2 * max3, max1 * min0 * min1)
        return a
