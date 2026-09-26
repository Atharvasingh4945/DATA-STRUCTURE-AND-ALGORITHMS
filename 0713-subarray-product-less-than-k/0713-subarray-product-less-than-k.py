class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<=1:
            return 0
        left=0
        count=0
        pro=1
        for right in range(len(nums)):
            pro*=nums[right]#window banayi
            while pro>=k:
                pro/=nums[left]#remove kr rahe hai
                left+=1#add ke rahe hai
            count+=right-left+1#update krr rahe hai
        return count
        