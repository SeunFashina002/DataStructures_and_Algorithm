# class Solution(object):
#     def runningSum(self, nums):
#         for i in range(1, len(nums)):
#             nums[i] = nums[i-1] + nums[i]
#         return nums


# sol = Solution()
# print(sol.runningSum([1, 2, 3, 4, 5]))


class Solution:
    def runningSum(self, nums):
        lst = []
        a = 0
        for i in nums:
            a += i
            lst.append(a)
        return lst

nums = [1,2,3,4,5]
sol = Solution()
print(sol.runningSum(nums))
