class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_value = -2
        next_value = -1
        
        for i in range(1, len(arr) + 1):
            max_value = max(max_value, next_value)
            next_value = arr[-i]
            arr[-i] = max_value
        return arr


