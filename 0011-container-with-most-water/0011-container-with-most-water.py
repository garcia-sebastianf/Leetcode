#Created by: Sebastián Felipe García Rojas

class Solution:
    def maxArea(self, height: List[int]) -> int:

        amountOfWater, MaxAmount = 0 , 0
        i , j = 0 , len(height)-1

        #Get a vector with the all posible values of amount of water.
        while i != j:

            if height[i] <= height[j]:
                amountOfWater = (j-i)*height[i]
                i += 1
                if amountOfWater > MaxAmount:
                    MaxAmount = amountOfWater
            else:
                amountOfWater = (j-i)*height[j]
                j -= 1
                if amountOfWater > MaxAmount:
                    MaxAmount = amountOfWater
        
        return MaxAmount

        
        

    

                        

        