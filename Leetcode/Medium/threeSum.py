def twoSum(nums,target):
        ans = []
        left = 0
        right = len(nums)-1
        cur = nums[left] + nums[right]
        while left < right:
            cur = nums[left] + nums[right]
            if cur == target:
                ans.append([nums[left],nums[right]])
            if cur > target:
                right -= 1
            else:
                left += 1
        return ans
def threeSum(nums,target):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    globalAns = {}
    nums = sorted(nums) #O(n log n)
    length = len(nums)
    # for i in range(length): #O(n^3)
    #     for j in range(i+1,length):
    #         for k in range(j+1,length):
    #             if nums[i] + nums[j] + nums[k] == 0:
    #                 cur = sorted([nums[i],nums[j],nums[k]])
    #                 if cur not in ans:
    #                     ans.append(cur)
    # for i in range(length):
    #     for j in range(i+1,length):
    #         target =  0 -nums[i] - nums[j]
    #         if target in nums:
    #             cur = sorted([nums[i],nums[j],target])
    #             if cur not in ans:
    #                 ans.append(cur)
    for i in range(length):
        target = 0 - nums[i]
        ansList = twoSum(nums,target)
        for ans in ansList :
            if i in ans:
                ansList.remove(ans)
            else:
                GlobalAns[sorted([nums[i],ans[0],ans[1]])] = True
    return GlobalAns.keys()
    
if __name__ == '__main__':
    nums =  [-1, 0, 1, 2, -1, -4]
    nums = sorted(nums)
    print(twoSum(sorted(nums),0))
    # return ans