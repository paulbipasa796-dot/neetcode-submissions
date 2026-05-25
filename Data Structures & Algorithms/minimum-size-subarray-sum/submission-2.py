class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlength=float('inf')
        summ=0
        l=0
        
        for r in range(len(nums)):
          summ+= nums[r]

          while summ >= target:
            minlength = min(minlength, r-l+1)
            summ -= nums[l]
            l+=1
        
        return minlength if minlength < float('inf') else 0
