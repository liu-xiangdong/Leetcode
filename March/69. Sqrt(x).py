class Solution:
    def mySqrt(self, x: int) -> int:
        left,right = 1,x
        mid = (left + right) // 2
        for i in range(x):
            if mid * mid == x:
                break
            elif mid * mid < x and (mid + 1) * (mid + 1) > x:
                break
            elif mid * mid > x:
                right = mid
                mid = (left + right) // 2
            else:
                left = mid
                mid = (left + right) // 2
        return mid
