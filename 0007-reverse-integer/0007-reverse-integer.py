class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n=False
        if x<0:
            n = True
            
        x=abs(x)
        if x==0:
            return 0
        digit=0
        while x>0:
            rem=x%10
            digit=digit*10+rem
            x=x//10
        if n==True:
            digit=digit*-1
        if -2**31>digit or 2**31-1<digit:
            return 0
        return digit
        

        
        