class Solution(object):
    def sortedSquares(self, nums):
        

        result =[]

        for num in nums:
            result.append(num ** 2)

            result.sort()

        return result