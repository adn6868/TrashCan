class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(nums)-1:
            if nums[i] <= nums[i+1]:
                count +=1
                i+=1
            else:
                break
        j = len(nums)-1
        while j > i+1:
            if nums[j] >= nums[j-1]:
                count +=1
                j -= 1
            else:
                break
        return len(nums) - count
            
        