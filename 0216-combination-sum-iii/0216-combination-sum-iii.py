class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result=[]
        self.solution(k,n,1,0,[])
        return self.result
    def solution(self,k,n,start,curr_sum,ans):
        if curr_sum==n and len(ans)==k:
            self.result.append(list(ans))
            return
        if curr_sum>n or len(ans)>k:
            return 
        for i in range(start,10):
            ans.append(i)
            self.solution(k,n,i+1,curr_sum+i,ans)
            ans.pop()

        
        