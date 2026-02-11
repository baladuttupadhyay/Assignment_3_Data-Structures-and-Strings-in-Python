#Calculate Factorial Using a Function
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Calling the function with sample number 5
number = 5
print("Factorial of ", number, "is", factorial(number))