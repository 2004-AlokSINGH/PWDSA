'''

ANSWER 1

class Solution:

  def findCommon(self,ar1, ar2, ar3):
    n1 = len(ar1)
    n2 = len(ar2)
    n3 = len(ar3)
    self.findCmn(ar1, ar2, ar3, n1, n2, n3)
    
  def findCmn(ar1, ar2, ar3, n1, n2, n3):
 
    # Initialize starting indexes for ar1[], ar2[] and ar3[]
    i, j, k = 0, 0, 0
 
    # Iterate through three arrays while all arrays have elements
    while (i < n1 and j < n2 and k < n3):
 
        # If x = y and y = z, print any of them and move ahead
        # in all arrays
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            print ar1[i],
            i += 1
            j += 1
            k += 1
 
        # x < y
        elif ar1[i] < ar2[j]:
            i += 1
 
        # y < z
        elif ar2[j] < ar3[k]:
            j += 1
 
        # We reach here when x > y and z < y, i.e., z is smallest
        else:
            k += 1

ANSWER 2

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # r=[]
        # a=[]
        # b=[]
        # for i in nums1:
        #     if i not in nums2 and i not in a:
        #         a.append(i)

        # for i in nums2:
        #     if i not in nums1 and i not in b:
        #         b.append(i)
        
        # r.append(a)
        # r.append(b)
         
        # return r

        a = set(nums1)
        b = set(nums2)

        return [a.difference(b), b.difference(a)]

  ANSWER 3

  class Solution:
    def transpose(self, matrix):
        n=len(matrix)
        c=len(matrix[0])
        ans = [[None] * n for _ in range(c)]
        for i in range(n):
           
            for j in range(c):
                ans[j][i]=matrix[i][j]
                
            
        return ans

ANSWER 4

class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        sum_ = 0
        for i in range(0,len(nums),2):
            sum_= sum_ + min(nums[i],nums[i+1])
        return sum_


ANSWER 5

class Solution():
    def arrangeCoins(self, n):
      return int(sqrt(2 * n + 0.25) - 0.50)


ANSWER 6
class Solution:
    def sortedSquares(self, nums) :
        l, r = 0, len(nums) - 1
        res = [0] * len(nums) # create a result list with dummy values
        i = len(nums) - 1 # index on which we will fill the result

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l]**2
                l += 1
            else:
                res[i] = nums[r]**2
                r -= 1
            i -= 1 # we have filled the result on this index, now we go to the index one lesser than this
        return res
'''
