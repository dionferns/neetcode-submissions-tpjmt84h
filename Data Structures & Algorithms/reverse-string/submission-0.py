class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
            reason to use two pointer algorithm:
            1. array in place. 
            2. question is about array. 
        """

        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            value = s[p2]
            s[p2] = s[p1]
            s[p1] = value
            p1 += 1
            p2 -= 1
        return s
        