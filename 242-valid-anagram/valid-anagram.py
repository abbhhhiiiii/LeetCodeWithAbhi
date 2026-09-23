class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False 

        count = {}

        for i in s:
            if i not in count:
                count[i] = 1 
            else:
                count[i] += 1 

        for i in t:
            if i not in count:
                return False

            else:
                count[i] -= 1

        for i in count:
            if count[i] != 0:
                return False

        return True       



        


        
        