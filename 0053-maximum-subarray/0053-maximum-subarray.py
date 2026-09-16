class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ''' ans = nums[0]
        for i in range(0, len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum = current_sum + nums[j]
                ans = max(ans, current_sum)
                if (current_sum < 0):
                    current_sum = 0
        return ans'''
        ans = nums[0]
        current_sum = 0
        for num in nums:
            current_sum += num
            ans = max(ans, current_sum)
            if current_sum < 0:
                current_sum = 0
        return ans

        