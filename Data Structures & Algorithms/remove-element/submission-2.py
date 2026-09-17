class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            if nums[l] != val:
                l += 1
            else:
                nums[l] = nums[r - 1]
                r -= 1
        return l