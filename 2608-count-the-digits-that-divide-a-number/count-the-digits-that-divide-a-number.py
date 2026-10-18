class Solution(object):
    def countDigits(self, num):
        count = 0

        for digit in str(num):
            digit = int(digit)

            if num % digit == 0:
                count += 1

        return count