class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, x in enumerate(nums):
            complement = target - x              # target minus current number
            if complement in seen:               # is the partner already in the notebook?
                return [seen[complement], i]           # partner's index, then current
            seen[x] = i                 # write current down for future
