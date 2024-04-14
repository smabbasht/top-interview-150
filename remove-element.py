class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)-1
        ind = 0
        while ind < len(nums) and ind <= k:
            if nums[ind] == val:
                if nums[k] != val:
                    nums[ind], nums[k] = nums[k], nums[ind]
                else:
                    ind -= 1
                k -= 1
            ind += 1

        return k+1
