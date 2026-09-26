class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(0,len(nums1)):
            j=0
            for j2 in range(0,len(nums2)):
                if nums2[j2]==nums1[i]:
                    j=j2
                    break
            found=False
            for k in range(j+1,len(nums2)):
                if nums2[k]>nums1[i]:
                    ans.append(nums2[k])
                    found=True
                    break
            if not found:
                ans.append(-1)
        return ans
        