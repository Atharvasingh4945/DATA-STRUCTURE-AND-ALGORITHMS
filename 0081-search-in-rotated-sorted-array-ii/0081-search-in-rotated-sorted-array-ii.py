class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        for i in range(0,len(nums)):
            if nums[i]==target:
                return True
        return False
        #but we have to do this in binary search to reduce the time complexity 
        ''' lo=0
            hi=len(nums)-1
            while(lo<=hi):
                mid=(lo+hi)//2
                if nums[mid]==target:
                    return True
                elif mid<target:
                    lo=mid+1
                else:
                    hi=mid-1
            return False
            def recursuve(target,nums,start):
                n=len(nums)
                if start>len(nums):
                    return False
                if nums(start)==target:
                    return True
                recusuve(target,nums,start+1)'''