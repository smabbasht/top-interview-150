class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        ind = 0
        while ind < len(nums)-1:
            if nums[ind+1] == nums[ind]:
                nums.pop(ind)
            else:
                ind += 1
        return len(nums)
