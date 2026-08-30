class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen=set()#this is how to create a empty set
        for num in nums:
            if num in seen:#== isliye nhi kyuki then two loops use hote and tc bhadti
                return True
            seen.add(num)
        return False
        