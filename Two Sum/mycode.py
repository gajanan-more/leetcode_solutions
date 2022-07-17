class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = dict()
        indexes = list()
        
        
        for i in range(len(nums)):
            sub = target-nums[i]

            if nums[i] in mapping:
                indexes.append(mapping[nums[i]])
                indexes.append(i)
                break
            else:
                mapping[sub]=i
        
        return indexes