class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 1:
            return 1
        a = len(nums)
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i]) 
                #删除这个元素后 后面元素向前一个位置 列表长度减1 
                continue
                #此处continue可以避免多个相同数字在一处的情况  即不增加i  在删除第i个元素后
                #向前移一个位置 相当于用一开始的第i个元素后面的第i+1个和第i+2个元素比较  避免漏比较
            else:
                i = i + 1
        return len(nums)
