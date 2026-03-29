class Solution:
    def isValid(self, s: str) -> bool:
        main_dict = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        stack = []
        for i in s:
            if i in main_dict:
                if stack and main_dict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        if len(stack) != 0:
            return False
        else:
            return True

