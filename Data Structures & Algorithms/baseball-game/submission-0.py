class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for val in operations: 
            
            if val == "+":
                scores.append(scores[-1] + scores[-2])

            elif val == 'D':
                scores.append(2 * scores[-1])

            elif val == 'C':
                scores.pop()

            else: 
                scores.append(int(val))

            print(scores)
        return sum(scores)