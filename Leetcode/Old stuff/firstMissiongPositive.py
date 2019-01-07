class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict ={ }
        for n in nums:
            if n >=0:
                dict[n] = True
        i = 0
        while i in dict.keys():
            i+=1
        return i