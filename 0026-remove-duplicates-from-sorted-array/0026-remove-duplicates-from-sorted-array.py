class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #result=[]
        count=0
        for i in range(0,len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                #result.append(nums[i])
                nums[count]=nums[i]#array overriding
                count+=1
        return count
                
# seee phle laga meko ek array return karni hai wihtout sorted element but then no of
#return krna hai kitni baar element repreat hua hai and yeah out of index jayega 

        