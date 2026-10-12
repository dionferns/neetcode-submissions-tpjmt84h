class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer_1 = 0
        pointer_2 = 1        

        while pointer_2 < len(nums):
            if nums[pointer_1] != nums[pointer_2]:
                nums[pointer_1 + 1 ] = nums[pointer_2]
                pointer_1 += 1
            else: 
                if not (nums[max(0, pointer_1 - 1)] == nums[pointer_2] and pointer_1 - 1 >= 0):
                    nums[pointer_1 + 1] = nums[pointer_2]
                    pointer_1 += 1
            pointer_2 += 1
        return pointer_1 + 1