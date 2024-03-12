class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        y=x[::-1]
        flag = True if x==y else False
        x=int(x)
        return flag
        