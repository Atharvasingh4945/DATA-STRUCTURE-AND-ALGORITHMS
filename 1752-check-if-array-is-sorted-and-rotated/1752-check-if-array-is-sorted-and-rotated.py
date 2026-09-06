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
        #ek rotate isliye count horha hai after one rotating if is gets correct position then then its sorted but if its not then sorted hogya hi nhii continuos rakhnaa hai array ko isliye 
        #Input: nums = [2,1,3,4] isme 1 galat hai toh after sorting 1342 hoga then 2 ayega starting mai kyuki continuos rakhnaa hai 2134 ho jayega