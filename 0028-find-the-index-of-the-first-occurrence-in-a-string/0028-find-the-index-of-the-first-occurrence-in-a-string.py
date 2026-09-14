class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n=len(haystack)
        m=len(needle)
        for i in range (n-m+1):#range isliye yeah otherm=wise out of index ho jata then problem hoti
            if haystack[i:i+m]==needle:#yha dheko slicing kari hai agar lagatar 3 indexes hai to return i 
                return i
        return -1
        