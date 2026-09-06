class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        drop=0
        for i in range (0,len(nums)):
            if nums[i]>nums[(i+1)%len(nums)]:# modulus helps us to check the last with the first index
                drop+=1
        return drop <= 1#this is not not right == is comparison and = is for assignment
        if drop>=1:
            return True
        else:
            return False
        #drop count krna hai less than pe 1 return krna hai and and drop kya hai kab array sorted nhi hai like going from 2 to 1 is a drop