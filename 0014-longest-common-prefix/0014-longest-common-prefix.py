# Longest Common Prefix
# Created by: Sebastián Felipe García Rojas

# Explicación lógica del programa:

# Para obtener el prefijo más largo común, basta con iterar sobre cada letra en la
# misma posición de cada string en la lista. Se compara la letra en la posición
# n de un string con la letra en la misma posición del string anterior. Si en alguna
# iteración las letras no coinciden, se detiene la comparación y se omite el prefijo
# a partir de esa posición. Así, se determina el prefijo más largo común a todos los strings.

# Logical explanation of the program:

# To find the longest common prefix, simply iterate over each letter at position
# n in the string and compare it with the letter at the same position in the previous
# string. If the condition where the two letters must be equal fails even once,
# proceed to ignore that letter and stop adding it to the prefix. This way, you
# determine the longest common prefix among all strings.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Initialize flags and variables

        commonLetterPrefix = True  # Flag to indicate if all strings have the same letter at current position
        previusLetter = ''         # Stores the previous letter for comparison
        once = False               # Flag to ensure the previous letter is set in the first iteration
        longestCommonPrefix = ""   # Result string to accumulate the longest common prefix
        
        
        for i in range(len(min(strs, key=len))):     # Iterate over each position in the shortest string
            for j in range(len(strs)):               # Iterate over each string in the list
                
                if len(strs) == 1:
                    return strs[j] 

                # Establish the previous letter in the first cycle of the loop
                if once == False:
                    previusLetter = strs[j][i]
                    once = True
                    continue

                # Compare current letter with previous letter
                if strs[j][i] != previusLetter:
                    commonLetterPrefix = False


                # Update the current letter to be the previous letter for the next iteration of the loop
                previusLetter = strs[j][i]
                           
            if commonLetterPrefix == True:

                # Add the prefix letter if all strings have the same letter at the n-th position
                longestCommonPrefix += strs[j][i]
                
                # Re-establish the flag to set the previous letter for the next n-th position in the first cycle
                once = False
            else:
                return longestCommonPrefix
               
        return longestCommonPrefix
                          
            
                
                