class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range (len(nums)):
            num=nums[i]
            sum_of_digit=0
            while num>0:
                digit=num%10
                sum_of_digit+=digit
                num=num//10
            if sum_of_digit==i:
                return i
        return -1
                
