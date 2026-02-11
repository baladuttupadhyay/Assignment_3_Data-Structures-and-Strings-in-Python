#Using the Math Module for Calculations
import math

user_input = int(input("Enter a number: "))
x = float(user_input)

# Calculate Square root of a number
sqrt_value = math.sqrt(x)

# Calculate Natural Logarithm (log base e) of the number

logarithm_value = math.log(x)

# Calculate sin of the number (in radians)
sin_value = math.sin(x)


print(f"Square root: {sqrt_value}")
print(f"Logarithm: {logarithm_value}")
print(f"Sin: {sin_value}")