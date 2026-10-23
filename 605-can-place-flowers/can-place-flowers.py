class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        
        count = 0

        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:

                left_khali = (i == 0 or flowerbed[i - 1] == 0)

                right_khali = (i == len(flowerbed) - 1 or flowerbed[i+1] == 0)

                if left_khali and right_khali:
                    flowerbed[i] = 1
                    count+=1

                if count >= n:
                    return True

        return count >= n