class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        original = x   # save the original number before we destroy x
        rev = 0         # initialize rev
        
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10
        
        if original == rev:
            return True
        else:
            return False