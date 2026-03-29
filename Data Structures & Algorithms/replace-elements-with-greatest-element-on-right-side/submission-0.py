class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            val_set = arr[i+1]
            for j in range(i+1, len(arr)):
                val_set = max(val_set, arr[j])

            arr[i] = val_set  

        arr[-1]  = -1
        return arr
