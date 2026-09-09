class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        '''nums=int(num)
        if (nums %2) != 0:
            return num
        else:
            for i in range(len(num)-1):
                if num[i]<num[i+1]:
                    max=num[i+1]
                else: 
                    max=num[i]
            return num
#it is not asking the elemeent it is asking the substring '''
        #isme prefix wapas karna hai toh like yha toh staring index yha ending index
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2 !=0:
                return num[:i+1]
        return ""
        