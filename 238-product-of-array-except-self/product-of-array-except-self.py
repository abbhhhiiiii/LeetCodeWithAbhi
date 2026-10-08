class Solution:
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)

        # Left product
        left = 1

        for i in range(len(nums)):
            answer[i] = left
            left = left * nums[i]

        # Right product
        right = 1

        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * right
            right = right * nums[i]

        return answer