class Solution:
    def isValid(self, s: str) -> bool:
        main_dict = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
        stack = []
        for i in range(0, len(s)):
            if len(stack) != 0:
                if stack[-1] in main_dict.keys():
                    if main_dict[stack[-1]] != s[i]:
                        stack.append(s[i])
                    else:
                        stack.pop(-1)
                else: 
                    stack.append(s[i])
            else:
                stack.append(s[i])

        if len(stack) != 0:
            return False
        else:
            return True

# goal is at the end of the iteration the stack list should get empty, this will happen if we pop all the closed brackets that we see. 
