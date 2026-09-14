class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.prove(candidates, target, 0, 0, [])
        return self.result

    def prove(self, candidates, target, start, curr_sum, ans):
        if curr_sum == target:
            self.result.append(list(ans))
            return
        if curr_sum > target:
            return
        for i in range(start, len(candidates)):
            ans.append(candidates[i])
            self.prove(candidates, target, i, curr_sum + candidates[i], ans)
            ans.pop()
            #toh kya kiya ki three sitution agar equal aya toh append karo in result if greater toh return karo and main jisme recursion work kr raha hai 