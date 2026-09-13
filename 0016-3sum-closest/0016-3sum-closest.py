class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """ 
        ''' so the basic is like 3 sum question we will have two var like clossest and the current value if closest is biggest then curr=closest and if it equals to valuse return current value elif left+1 else right -1 '''
        nums.sort()
        n=len(nums)
        closest_val=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            left=i+1
            right=n-1
            while left < right :
                current_val=nums[i]+nums[left]+nums[right]
                if abs(current_val-target)<abs(closest_val-target):
                    closest_val=current_val
                if current_val==target:
                    return current_val
                elif current_val<target:
                    left+=1
                else:
                    right-=1
        return closest_val

        