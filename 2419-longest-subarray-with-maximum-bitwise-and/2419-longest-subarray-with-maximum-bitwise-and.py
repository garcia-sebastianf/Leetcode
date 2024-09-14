# Created by: Sebastián Felipe García Rojas

class Solution:
    def longestSubarray(self, nums): 
        # Encuentra el máximo valor en el array
        max_value = max(nums)
    
        max_len = 0
        current_len = 0
        
        # Recorre el array
        for num in nums:
            # Si el número AND con el valor máximo es igual al valor máximo
            if (num & max_value) == max_value:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0
        
        return max_len
        