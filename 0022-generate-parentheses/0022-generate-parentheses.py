class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """#normally aise nhi ahra hai ek result naam ka var use hi krna padega 
        self.result=[]
        self.Parentheses(n,0,0,"")
        return self.result
    def Parentheses(self,n,open,close,ans):
        if open ==n and close ==n:
            self.result.append(ans)
            return
        if open>n or close>open:
            return
        self.Parentheses(n,open+1,close,ans+"(")
        self.Parentheses(n,open,close+1,ans+")")
        