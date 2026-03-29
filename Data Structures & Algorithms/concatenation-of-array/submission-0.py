class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        val = []
        for i in [1,2]:
            for num in nums:
                val.append(num)
        return val