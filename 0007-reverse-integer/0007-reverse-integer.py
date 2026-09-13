class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative =x<0 #x<0 this is a boolean value like condition ke upaar hai
        x=abs(x)
        rev=0
        while x>0:
            digit=x%10
            x=x//10
            rev=rev*10+digit
        if negative:
            rev=-rev
        if rev < -2**31 or rev > 2**31 - 1:# range ki bakchodi hai
            return 0
        return rev

        