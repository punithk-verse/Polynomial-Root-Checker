polynomial = input("Enter the polynomial in terms of x (e.g., x**2 - 3*x + 2): ")
x = float(input("Enter the value of x: "))
# Evaluate the polynomial
result = eval(polynomial)
# Output result
if result == 0:
    print("Yes, P(x) = 0. It's a root.")
else:
    print(f"No, P(x) = {result}. Not a root.")
# learnt about eval , hope to update even with rational root theorem
