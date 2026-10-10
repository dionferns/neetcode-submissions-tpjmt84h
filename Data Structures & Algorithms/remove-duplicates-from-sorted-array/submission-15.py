class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Why two pointer approach: says already sorted, it's about array, says remove duplicate"""

        pointer_1, pointer_2 = 0, 1

        while pointer_2 < len(nums):
            if nums[pointer_1] != nums[pointer_2]:
                nums[pointer_1+1] = nums[pointer_2]
                pointer_1 += 1
            pointer_2 += 1

        return pointer_1 + 1