class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #so the approach is like 1)3 indexes 0n3 but what if we can 2)sorting then index + index-1 + index +1
        nums.sort()
        n=len(nums)
        result=[]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue #taaki duplicates ke aage move kare
            left=i+1
            right=n-1
            target=-nums[i]
            '''nums[i] + nums[left] + nums[right] = 0
            nums[left] + nums[right] = 0 - nums[i]
            nums[left] + nums[right] = -nums[i]'''
            while left<right:
                current_sum=nums[left]+nums[right]
                if current_sum==target:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:#chechking duplicates and moving forward
                        left+=1
                    while left <right and nums[right]==nums[right+1]:
                        right-=1
                elif current_sum<target:
                    left+=1
                else:
                    right-=1
        return result
'''see if == then print krwaya and aage move krwaya
    see if < current chota hai then target left ko move krwaya
    see if > yeah hai toh target bada hai then right ko move krwayenge'''


        