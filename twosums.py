# solved
nums = [1,1,3,3,5,9]
target = 2

class Solution:
    def twoSum(self, nums,target):
        things = {}
        for index, i in enumerate(nums):
            num2 = target - i
            if num2 in things:
                return [things[num2], index]
            else: things[i] = nums.index(i)




a = Solution()
print a.twoSum(nums, target)
