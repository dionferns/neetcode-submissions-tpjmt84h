class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones_total = 0
        temp = 0
        for i in nums: 
            if i == 1:
                temp += 1
            else: 
                ones_total = max(temp, ones_total)
                temp = 0
                    
        return max(ones_total, temp)
