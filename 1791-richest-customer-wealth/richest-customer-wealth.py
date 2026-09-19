class Solution(object):
    def maximumWealth(self, accounts):

        maxwealth = 0

        for customers in accounts:
            wealth = sum(customers)

            if wealth >= maxwealth:
                maxwealth = wealth

        return maxwealth

        