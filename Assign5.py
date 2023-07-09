'''
Answer 1
class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        k=0
        i=0
        b=[]
        org=original
        l=len(org)
        if m*n!=l:
            return []
        while i<(l):
            a=[]
            for j in range(n):
                a.append(org[k])
                k=k+1
            b.append(a)
            i=i+n
        return b

Answer 2

class Solution():
    def arrangeCoins(self, n):
        completeStairs = 0
        start = 1
        end = n

        while start <= end:
            mid = start + (end - start) // 2
			# How many coins required to completely fill 'mid' rows?
			# Use Gauss Summation to find that in O(1) time
            if (mid * ( mid + 1)) // 2 <= n:
                completeStairs = mid
                start = mid + 1
            else:
                end = mid - 1


        return completeStairs


Answer 3

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

Answer 4

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


Answer 5

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
    
        n=len(arr1)
        k=n
        m=len(arr2)
        for i in arr1:
            for j in arr2:
                dd=i-j
                if abs(dd)>d :
                    continue
                else:
                    k=k-1
                    break
        return k

Answer 6

# class Solution(object):
#     def findDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """

# 
class Solution:
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            n = abs(num)
            if nums[n - 1] < 0:
                res.append(n)
            nums[n - 1] = -nums[n - 1]
        return res

Answer 8


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        
        
        a=[]
        ch=changed
        ch.sort()
        n=len(ch)


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




'''
