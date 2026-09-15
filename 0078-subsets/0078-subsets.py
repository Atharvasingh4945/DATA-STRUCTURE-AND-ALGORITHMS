class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.subsequence(nums, [])
        return self.result

    def subsequence(self, nums, ans):
        if len(nums) == 0:
            self.result.append(list(ans))
            return
        ch = nums[0]
        rest = nums[1:]
        self.subsequence(rest, ans)
        self.subsequence(rest, ans + [ch])