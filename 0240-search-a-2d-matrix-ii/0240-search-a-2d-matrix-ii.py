class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row=0
        col=len(matrix[0])-1
        while(row<len(matrix) and col>=0):#row se bahar na jaaye and col>0
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:#order aisa hai ki left jayega to smaller number and niche toh bada number
                col=col-1
            else:
                row =row+1
        return False

        