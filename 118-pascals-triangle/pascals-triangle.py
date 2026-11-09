class Solution(object):
    def generate(self, numRows):
        
        result = []

        previous = []

        for i in range(numRows):

            row = [1]

            for j in range(len(previous) -1 ):
                row.append(previous[j] + previous[j + 1])

            if i > 0:
                row.append(1)

            result.append(row)

            previous = row 
        
        return result