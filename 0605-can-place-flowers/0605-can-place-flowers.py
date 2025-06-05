class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        j = 1
        while(i < len(flowerbed) and n > 0):
            
            if(flowerbed[i] == 1):
                j = 0;
            else:
                j += 1
                if(j == 3):
                    n -= 1
                    j = 1
            i += 1
        if(n == 0 or (n == 1 and j == 2)):
            return True
        return False
                
        