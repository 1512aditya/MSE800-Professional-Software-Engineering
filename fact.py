def factorial_while(n):
    
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        i = 1
        while i <= n:
            result *= i  
            i += 1       
        return result

number = 4
fact = factorial_while(number)
print(f"The factorial of {number} is: {fact}")