class Solution(object):
    def isIsomorphic(self, s, t):

        if len(s) != len(t):
            return False

        mapping = {}
        reverse = {}

        for i, j in zip(s, t):

            if i not in mapping:
                mapping[i] = j
            else:
                if mapping[i] != j:
                    return False

            if j not in reverse:
                reverse[j] = i
            else:
                if reverse[j] != i:
                    return False

        return True