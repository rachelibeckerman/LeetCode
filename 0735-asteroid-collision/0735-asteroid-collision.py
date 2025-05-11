class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        while i < len(asteroids):
            if(asteroids[i] < 0):
                j = i -1
                while(j >= 0):
                    if(asteroids[j] > 0):
                        if(abs(asteroids[i]) > abs(asteroids[j])):
                            del asteroids[j]
                            i -= 1
                        elif(abs(asteroids[i]) == abs(asteroids[j])):
                            del asteroids[i]
                            del asteroids[j]
                            i -= 2
                            break
                        else:
                            del asteroids[i]
                            i -= 1
                            break
                    j -= 1
            i += 1
                    
        return asteroids