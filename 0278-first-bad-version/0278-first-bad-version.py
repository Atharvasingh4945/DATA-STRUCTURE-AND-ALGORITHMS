# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo=1
        hi=n
        while(lo<=hi):
            mid=(lo+hi)//2
            if isBadVersion(mid)==True:#if bad that means the bad part start before the midd so high is -1 to middle
                ans=mid
                hi=mid-1
            else:#if false then the bad is at more than the middle part so low will be moved
                lo=mid+1
        return lo

        