class Solution(object):
    def sortedSquares(self, nums):

        left = 0
        right = len(nums) - 1
        i = len(nums) - 1

        result = [0] * len(nums)

        while left <= right:

            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[i] = left_square
                left += 1
                i -= 1

            else:
                result[i] = right_square
                right -= 1
                i -= 1

        return result