#Created by: Sebastián Felipe García Rojas

#n = 2     #Number to evaluate: Is happy?

def Separate_digits(num: int):
    digits = []

    for i in str(num):
        digits.append(int(i))
        
    return digits

def Sum_of_squares(digits):
    sum_of_squares = 0

    for Number in digits:
        sum_of_squares = sum_of_squares + Number**2

    return sum_of_squares

class Solution:
    def isHappy(self, n: int) -> bool:

        resultNumber = 0 # Registers the sum of the square of the digits}
        happynumber_result = False
        Repeat = 7 #Number the times the process is repetead before determined happiness

        for i in range(Repeat):
            digits_list = Separate_digits(n)
            result_sum_of_squares = Sum_of_squares(digits_list)

            if(result_sum_of_squares == 1):
                happynumber_result = True
                return happynumber_result

            n = result_sum_of_squares  

        return happynumber_result

#Happy_number = Solution()
#Happy_number.isHappy(n) 
 
            