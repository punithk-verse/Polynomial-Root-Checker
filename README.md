# Polynomial-Root-Checker
his project helps users understand how to evaluate a polynomial at a given value of `x` and verify if it’s a root.   It’s a great beginner-friendly exercise for learning about **polynomials, roots, and Python expression evaluation**.  ---
# 🔢 Polynomial Root Checker — Using the Rational Root Theorem

A simple Python program that checks whether a given number is a **root of a polynomial** and explains the **Rational Root Theorem** used to predict possible rational roots.
---
## 🧮 About the Project
This project helps users understand how to evaluate a polynomial at a given value of `x` and verify if it’s a root.  
It’s a great beginner-friendly exercise for learning about **polynomials, roots, and Python expression evaluation**.

---

## 🚀 Features
- Accepts any polynomial input (e.g. `x**3 - 4*x**2 + x + 6`)
- Evaluates the polynomial at a given value of `x`
- Checks if the result is `0` (i.e., whether it’s a root)
- Simple and interactive command-line interface

---

## 🧠 How It Works
1. The user enters a polynomial expression such as:
 **Write your polynomial** in standard form, for example:  
   \[
   P(x) = 4x^4 - 12x^3 - 9x^2 + 27x - 18
   \]

2. **Apply the Rational Root Theorem** manually or by logic:
   - Find all factors of the **constant term** (last number)
   - Find all factors of the **leading coefficient** (first number)
   - Form all possible rational roots = ±(factors of constant) ÷ (factors of leading coefficient)

   Example:  
   Constant = -18 → factors = ±1, ±2, ±3, ±6, ±9, ±18  
   Leading = 4 → factors = ±1, ±2, ±4  
   Possible roots = ±1, ±1/2, ±1/4, ±2, ±3, ±3/2, ±3/4, ±6, ±9, ±9/2, ±9/4, ±18, ±18/2, ±18/4

3. **Use the Python code** to test each possible root:
   - Run your program
   - Enter the polynomial:  
     '''
     4*x**4 - 12*x**3 - 9*x**2 + 27*x - 18
   '''
   - Enter one possible root at a time (like `1`, `1.5`, `-3`, etc.)
   - The program will tell you:
     ```
     Yes, P(x) = 0. It's a root.
     ```
     or
     ```
     No, P(x) = value. Not a root.
     ```

4. **Identify the true roots** — the values of `x` that make `P(x) = 0`.

---
