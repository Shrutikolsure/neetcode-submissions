class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #nums.sort()
        #for i in range(len(nums) - 1):
        #    if nums[i] == nums[i+1]:
        #        return True
        #return False
        nums.sort()
        n = len(nums)
        nums_1=len(set(nums))
        if n == nums_1:
            return False
        return True