# class Solution(object):
#     def pivotIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         sumL = 0
#         sumR = sum(nums)
#         for i in range(len(nums)):
#             sumR -= nums[i]
#             if sumL == sumR:
#                 return i
#             sumL += nums[i]
#         return -1

# nums = [1,7,3,6,5,6]
# sol = Solution()
# print(sol.pivotIndex(nums))


"""
An index is said to be pivot when the sum of the array to the left is the same as the sum of the array to 
the right.
"""

class Solution:
    def pivotIndex(self, nums):
        sumLeft = 0
        lst_total = sum(nums)
        sumRight = lst_total
        
        for i in range(len(nums)):
            sumRight -= nums[i]
            if sumLeft == sumRight:
                return i
            sumLeft += nums[i]
        return -1

nums = [1,7,3,6,5,6]
sol = Solution()
print(sol.pivotIndex(nums))

