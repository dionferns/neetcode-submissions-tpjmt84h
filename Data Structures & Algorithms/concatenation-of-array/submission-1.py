class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        main = [0] * 2 * len(nums)
        for i in range(len(nums)):
            main[i] = nums[i]
            main[i + len(nums)] = nums[i]
        return main