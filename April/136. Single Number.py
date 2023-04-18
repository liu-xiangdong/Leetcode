"""class Solution:
    def singleNumber(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            result = dict()
            nums2 = list()
            for i in nums:
                if i in result:
                    result[i] = result[i] + 1
                else:
                    result[i] = 1
                    nums2.append(i)
            for j in nums2:
                if result[j] ==1:
                    return j
"""
class Solution:
    def singleNumber(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            nums2 = []
            for i in nums:
                if i in nums2:
                    nums2.remove(i)
                else:
                    nums2.append(i)
            return nums2[0]
