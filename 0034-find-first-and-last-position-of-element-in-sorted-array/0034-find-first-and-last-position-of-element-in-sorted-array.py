class Solution(object):
    def binary_search(self, nums, target,first_find):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo=0
        hi=len(nums)-1
        result=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:#ispe aaye the kya kiya humne hum aage piche move krenge to find the value 
                result=mid
                if first_find:
                    hi=mid-1
                else:
                    lo=mid+1
            elif nums[mid]<target:
                lo=mid+1
            else:
                hi=mid-1
        return result

    def searchRange(self,nums,target):
        left =self.binary_search(nums, target, True)
        if left == -1:
            return [-1, -1]
        right = self.binary_search(nums, target, False)
        return [left, right]   