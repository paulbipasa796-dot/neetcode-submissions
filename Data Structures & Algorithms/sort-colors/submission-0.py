class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {}
        
        for num in nums:
            count[num] = 1+ count.get(num,0)
        index = 0

        for color in range(3):
            c = count.get(color,0)
            for i in range(c):
                nums[index] = color
                index += 1
            
            