class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        #question khera ki 0 index wali string ko right mai bhejo agar solution mile to true brna false 
        # we use trick like s+s will have all the substring possible 
        '''
        if len(s)!=len(goal):
            return False
        #if goal in (s+s):
        #    return True
        #but null nhi return krega yeah toh basic pe hi jana padega
        n=len(s)
        for i in range(n):
            shifted=s[i:]+s[:i]
            if shifted==goal:
                return True
        return False   '''
        if len(s) != len(goal):
            return False

        if goal in (s + s):
            return True
        else:
            return False