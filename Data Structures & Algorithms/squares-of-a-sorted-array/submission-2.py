class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Two pointer approach because: 1. It's an array, 2. already sorted, 3. question asks for "rearrange". 

        l, r = 0, len(nums) - 1
        array = []
        
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2: 
                array.append(nums[r] ** 2)
                r -= 1
            else: 
                array.append(nums[l] ** 2)
                l += 1

        return array[::-1]