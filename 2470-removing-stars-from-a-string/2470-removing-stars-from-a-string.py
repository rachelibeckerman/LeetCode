class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        answer = ""
        for i in s:
            if(i == "*"):
                stack.pop()
            else:
                stack.append(i)
        for i in stack:
            answer += i          
           
        return answer

        