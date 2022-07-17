class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checkArray = {}
        for i in range(len(nums)):
            num_we_want = target - nums[i]
            if num_we_want in checkArray:
                return [checkArray[num_we_want], i]
            else:
                checkArray[nums[i]] = i