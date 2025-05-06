class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        i = 0
        for i in range(min(len(word1),len(word2))):
            answer += word1[i]
            answer += word2[i]
        answer += max(word1[i+1:] , word2[i+1:])
        return answer
       
        