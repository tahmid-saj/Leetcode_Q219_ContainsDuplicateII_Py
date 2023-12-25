class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == 1: return
        prev = {}

        for i in range(0, len(nums)):
            if not nums[i] in prev.keys(): prev[nums[i]] = i
            else:
                if abs(i - prev[nums[i]]) <= k: return True
                else: prev[nums[i]] = i

        return False
