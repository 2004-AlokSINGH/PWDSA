''' ANSWER 1

class Solution:
    def threeSumClosest(self, arr, target):
        # Sort the elements
        arr.sort()
        resultSum = arr[0] + arr[1] + arr[2]
        minDifference = float('inf')

        # Now fix the first element and find the other two elements
        for i in range(len(arr) - 2):
            # Find other two elements using Two Sum approach
            left = i + 1
            right = len(arr) - 1

            while left < right:
                sum_val = arr[i] + arr[left] + arr[right]

                if sum_val == target:
                    return target
                if sum_val < target:
                    left += 1
                else:
                    right -= 1

                diffToTarget = abs(sum_val - target)
                if diffToTarget < minDifference:
                    # update the result sum
                    resultSum = sum_val
                    minDifference = diffToTarget

        return resultSum
ANSWER 2
class Solution:
    
    def fourSum(self,nums: List[int], target: int) -> List[List[int]]:
        n = len(nums) # size of the array
        ans = []

    # sort the given array:
        nums.sort()

    # calculating the quadruplets:
        for i in range(n):
        # avoid the duplicates while moving i:
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
            # avoid the duplicates while moving j:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

            # 2 pointers:
                k = j + 1
                l = n - 1
                while k < l:
                    _sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if _sum == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(temp)
                        k += 1
                        l -= 1

                    # skip the duplicates:
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif _sum < target:
                        k += 1
                    else:
                        l -= 1

        return ans
ANSWER 8
class Solution:
    def merge(self, intervals):
        # intervals.sort(key=lambda x: x[0])
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

ANSWER 3


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # To find next permutations, we'll start from the end
        i = j = len(nums)-1
        # First we'll find the first non-increasing element starting from the end
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # After completion of the first loop, there will be two cases
        # 1. Our i becomes zero (This will happen if the given array is sorted decreasingly). In this case, we'll simply reverse the sequence and will return 
        if i == 0:
            nums.reverse()
            return 
        # 2. If it's not zero then we'll find the first number grater then nums[i-1] starting from end
        while nums[j] <= nums[i-1]:
            j -= 1
        # Now out pointer is pointing at two different positions
        # i. first non-assending number from end
        # j. first number greater than nums[i-1]
        
        # We'll swap these two numbers
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # We'll reverse a sequence strating from i to end
        nums[i:]= nums[len(nums)-1:i-1:-1]
        # We don't need to return anything as we've modified nums in-place

  ANswer 4

  class Solution(object):
    def searchInsert(self, nums, target):
        start, end = 0, len(nums) - 1
        ans = len(nums) # Default answer when target is greater than all elements
        
        while start <= end:
            mid = (start + end) / 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                ans = mid # Update the answer to the current index
                end = mid - 1
                
        return ans


Answer 5

class Solution(object):
    def plusOne(self, digits):
        self.d=digits
        a=""
        for i in digits:
            a=a+str(i)
        s=int(a)+1
        b=[]
        for i in str(s):
            b.append(int(i))
        return b

Answer 6

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        xor=0
        for i in nums:
            xor=xor^i
        return xor

  Answer 7

  class Solution():
    def mr(self,nums, lower, upper):
        result = []
    
        if lower < nums[0]:
            result.append([lower, nums[0] - 1])
    
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] + 1:
                result.append([nums[i-1] + 1, nums[i] - 1])
    
        if upper > nums[-1]:
            result.append([nums[-1] + 1, upper])
    
        return result

Answer 8


class Solution:
    def merge(self, intervals):
        # intervals.sort(key=lambda x: x[0])
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
        '''
