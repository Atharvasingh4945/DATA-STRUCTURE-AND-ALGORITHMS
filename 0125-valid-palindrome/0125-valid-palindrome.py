class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''isalnum() what is this

isalnum() is a built-in Python string method that checks whether a character (or string) is alphanumeric — meaning it's either a letter (a-z, A-Z) or a digit (0-9). it returns true or false'''
        left=0
        n=len(s)
        right=n-1
        while left<right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True

#teen case right!= left 2) left leliya 3) right leliya