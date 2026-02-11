
# Python Assignments: Factorial & Math Module Calculations

This repository contains two simple Python programs:

1. **Assignment_3_Task1_Functions & Modules in Python.py** – Calculates the factorial of a number using a function and prints the result for a sample input.
2. **Assignment_3_Task2_Using the Math Module for Calculations.py** – Prompts the user for a number and uses Python's built-in `math` module to compute the square root, natural logarithm (base *e*), and sine (in radians).

---

## 1) Factorial Program
**File:** `Assignment_3_Task1_Functions & Modules in Python.py`

### Description
Defines a function `factorial(n)` that calculates the factorial of a non‑negative integer using a loop and returns the value. The program then calls the function with a sample number (5) and prints the output.

### Code (as used in the file)
```python
# Calculate Factorial Using a Function

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Calling the function with sample number 5
number = 5
print("Factorial of ", number, "is", factorial(number))
```

### Expected Output
```
Factorial of  5 is 120
```

> **Note:** You can change the `number` variable to compute the factorial of other non‑negative integers. For large values, consider using Python's big integers (built-in) but be aware the output grows rapidly.

---

## 2) Math Module Calculations Program
**File:** `Assignment_3_Task2_Using the Math Module for Calculations.py`

### Description
Prompts the user for a number and computes:
- Square root (`math.sqrt`) – defined for input ≥ 0
- Natural logarithm, base *e* (`math.log`) – defined for input > 0
- Sine in radians (`math.sin`) – defined for all real numbers

### Code (as used in the file)
```python
# Using the Math Module for Calculations
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
```

### Example Run
**Input:** `25`
```
Enter a number: 25
Square root: 5.0
Logarithm: 3.2188758248682006
Sin: -0.13235175009777303
```

> **Validation Tips:**
> - For negative inputs, `math.sqrt(x)` will raise a `ValueError`. Use a guard like `if x >= 0` before calling `sqrt`.
> - For non‑positive inputs, `math.log(x)` will raise a `ValueError`. Use `if x > 0` before calling `log`.
> - `math.sin(x)` accepts any real number (in **radians**). If you have degrees, convert with `math.sin(math.radians(deg))`.

---
**Author:** Baldutt Upadhyay
