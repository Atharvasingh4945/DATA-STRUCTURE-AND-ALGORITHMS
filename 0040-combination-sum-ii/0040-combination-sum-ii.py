class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.result=[]
        self.solve(candidates,target,0,0,[])
        return self.result
    def solve(self,candidates,target,start,curr_sum,ans):
        if curr_sum==target:
            self.result.append(list(ans))
            return
        if curr_sum>target:
            return
        for i in range(start,len(candidates)):
            if i>start and candidates[i]==candidates[i-1]:#to remove the duplicates
                continue
            ans.append(candidates[i])
            self.solve(candidates,target,i+1,curr_sum+candidates[i],ans)
            ans.pop()
        