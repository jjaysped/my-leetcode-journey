class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()            # empty set
        for x in nums:
            if x in seen:             # have I seen x before?
                return True
            seen.add(x)                # add x to the set
        return False
