class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        main_list = []
        for i in nums:
            if i in main_list:
                return True
            else:
                main_list.append(i)
        return False