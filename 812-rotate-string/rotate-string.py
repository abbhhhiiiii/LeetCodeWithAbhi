class Solution(object):
    def rotateString(self, s, goal):

        if len(s) != len(goal):
            return False

        new_s = s + s 

        return goal in new_s

            

            
        
        