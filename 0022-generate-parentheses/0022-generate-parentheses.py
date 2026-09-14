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
        """Before a function call (self.Parentheses(...)): tells Python "call the Parentheses method that belongs to this object," so it can find it and auto-pass self into it too.
Before a variable (self.result): tells Python "store/access this on this object," not as a local variable that disappears when the function ends. That's why self.result set in generateParenthesis is still visible inside Parentheses — both are looking at the same object's attribute, not separate local scopes."""