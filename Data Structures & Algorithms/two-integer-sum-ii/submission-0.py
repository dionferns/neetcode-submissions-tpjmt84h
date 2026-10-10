class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]

        # Solution one: using hashmap to store the values of different index in the array. 

        # Solution two: nested loop going from left to right. 

        #Solution three(optimal): two pointer: one on the left, one of the right, 
        increase the  left pointer/decrease the  right pointer to get the sum of the values these pointers are at to be   
        closer to the target value. 
        """

        #Optimal solution.

        pointer_1 = 0
        pointer_2 = len(numbers) - 1

        while pointer_1 < pointer_2:
            pointer_sum = numbers[pointer_1] + numbers[pointer_2]
            if pointer_sum > target:
                pointer_2 -= 1 
            elif pointer_sum < target:
                pointer_1 += 1 
            else: 
                return [pointer_1 + 1, pointer_2 + 1]

        if pointer_sum == target: 
            return [pointer_1 + 1, pointer_2 + 1]
        
        return -1

        
