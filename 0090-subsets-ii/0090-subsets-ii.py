class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.result = []
        self.subsequence(nums, 0, [])
        return self.result

    def subsequence(self, nums, start, ans):
        self.result.append(list(ans))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            ans.append(nums[i])
            self.subsequence(nums, i+1, ans)
            ans.pop()