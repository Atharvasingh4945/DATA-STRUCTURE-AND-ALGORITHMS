class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #arr=[]
        #for i in range (0,len(nums)):
        #    if nums[i]!=0:
        #        arr.append(nums[i])
        #n=len(nums)-len(arr)
        #for i in range (n):
        #    arr.append(0)
        #for i in range(len(nums)):
        #    nums[i]=arr[i]
        #but this will not work kyuki that you must do this in-place without making a copy of the array
        
        # ab kya kaare 2 pointer se array overwrite krenge
        pos=0
        for i in range(0,len(nums)):# ab  non zero element ko aage push krenge with array overwriting
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+=1
        for i in range(pos,len(nums)):#for zeroes
            nums[i]=0