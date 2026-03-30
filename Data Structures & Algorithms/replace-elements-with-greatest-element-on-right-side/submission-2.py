class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        right_max = -1

        for i in range(len(arr) - 1, -1, -1):
            next_val = max(arr[i],right_max)
            arr[i] = right_max
            right_max = next_val

        return arr
            

