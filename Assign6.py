'''
Answer 1

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = []
        a , b = 0 , len(s)
        
        for i in s:
            if(i == 'I'):
                ans.append(a)
                a += 1
            else:
                ans.append(b)
                b -= 1
        
        if(s[-1] == 'D'):
            ans.append(a)
        else:
            ans.append(b)
                       
        return ans

Answer 2

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])

        if m==0:
            return False
        
        high=m*n-1
        low=0
        while(low<=high):
            midIdx=low+(high-low)//2 #high/2
            rowIdx=midIdx//n 
            colIdx=midIdx%n
            midele=matrix[rowIdx][colIdx]

            if midele==target:
                return True
            
            elif target<midele:
                high=midIdx-1
            else:
                low=midIdx+1
        return False

Answer 3


class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1


Answer 4

class Solution:
    def findMaxLength(self, nums):
        # nums.sort()
        c=0
        Z=0
        o=0
        for i in nums:
            if i == 1:
                o=o+1

            else:
                Z=Z+1
            
            if o-Z==0:
                c=c+(2*o)
                o=0
                Z=0
        return c

Answer 5

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n, res = len(nums1), 0
        for i in range(n):
            res += nums1[i] * nums2[n - i - 1]
        return res


Answer 6

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        
        
        a=[]
        ch=changed
        changed.sort()
        n=len(changed)


        if n%2!=0:
            return []

        c=Counter(ch)


        for i in ch:
            if i in c and c[i]>=1:
                c[i]=c[i]-1
                if i*2 in c and c[i*2]>=1:
                    a.append(i)
                    c[i*2]-=1


            if len(a)==n//2:
                return a
Answer 7

class Solution:
    def generateMatrix(self, n):
        # Declaration
        matrix = [[0] * n for _ in range(n)]
        
        # Edge Case
        if n == 0:
            return matrix
        
        # Normal Case
        rowStart = 0
        rowEnd = n - 1
        colStart = 0
        colEnd = n - 1
        num = 1
        
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart, colEnd + 1):
                matrix[rowStart][i] = num
                num += 1
            rowStart += 1
            
            for i in range(rowStart, rowEnd + 1):
                matrix[i][colEnd] = num
                num += 1
            colEnd -= 1
            
            for i in range(colEnd, colStart - 1, -1):
                if rowStart <= rowEnd:
                    matrix[rowEnd][i] = num
                    num += 1
            rowEnd -= 1
            
            for i in range(rowEnd, rowStart - 1, -1):
                if colStart <= colEnd:
                    matrix[i][colStart] = num
                    num += 1
            colStart += 1
        
        return matrix
'''
