class Solution:
    def isSubsequence(self, s, t):
        left = 0

        for right in range(len(t)):
            if left < len(s) and s[left] == t[right]:
                left += 1

        return left == len(s)