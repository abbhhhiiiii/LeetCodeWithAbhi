class Solution(object):
    def findMaxAverage(self, nums, k):

        arr_sum = sum(nums[:k])
        max_sum = arr_sum


        for i in range(len(nums) - k):
            arr_sum = arr_sum - nums[i] + nums[i+k]

            max_sum = max(max_sum, arr_sum)

        return float(max_sum) / k
        