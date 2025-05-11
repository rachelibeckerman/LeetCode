class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # i = 0
        # while i < len(asteroids):
        #     if(asteroids[i] < 0):
        #         j = i -1
        #         while(j >= 0):
        #             if(asteroids[j] > 0):
        #                 if(abs(asteroids[i]) > abs(asteroids[j])):
        #                     del asteroids[j]
        #                     i -= 1
        #                 elif(abs(asteroids[i]) == abs(asteroids[j])):
        #                     del asteroids[i]
        #                     del asteroids[j]
        #                     i -= 2
        #                     break
        #                 else:
        #                     del asteroids[i]
        #                     i -= 1
        #                     break
        #             j -= 1
        #     i += 1
        stack = []
        for a in asteroids:
            while(stack and a < 0 and stack[-1] > 0 ):
                    if(stack[-1] < abs(a)):
                        stack.pop()
                        continue
                    elif(stack[-1] == abs(a)):
                        stack.pop()
                    break
            else:
                stack.append(a)
        return stack