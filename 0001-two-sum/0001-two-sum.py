class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''for i in range(0,len(nums)):
            if nums[i]+nums[i+1]==target:
                return i,i+1'''
                #this is error 1)indexout of bound 2)only taking adjacent inexes
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
        