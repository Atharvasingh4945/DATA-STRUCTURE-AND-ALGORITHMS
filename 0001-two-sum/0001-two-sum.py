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
        '''i=0 (nums[0]=3):
j=1: 3+5=8 ≠ 9
j=2: 3+2=5 ≠ 9
j=3: 3+7=10 ≠ 9
i=1 (nums[1]=5):
j=2: 5+2=7 ≠ 9
j=3: 5+7=12 ≠ 9
i=2 (nums[2]=2):
j=3: 2+7=9 ✅ match! → return [2,3]'''