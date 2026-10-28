class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word = []
        for i in range(0, max(len(word1), len(word2))):
            if i < len(word1):
                word.append(word1[i])
            if i < len(word2):
                word.append(word2[i])
        return "".join(word)