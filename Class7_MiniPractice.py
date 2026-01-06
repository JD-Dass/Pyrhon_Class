# Even / Odd
# num = float(input("Enter number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# simple calculator
print("""
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division
      """)

choice = (input("Choose operation (1 to 4): "))
num1 = float(input("Enter Number One: "))
num2 = float(input("Enter Number Two: "))

if choice == "1":
    print(f"ADD: {num1 + num2}")
elif choice ==  "2":
    print(f"SUB: {num1 - num2}")
elif choice ==  "3":
    print(f"MULTIPLY: {num1 * num2}")
elif choice ==  "4":
    if num2 != 0:
        print(f"DIVIDE: {num1 / num2}")
    else:
        print("Divition by zero not allowed")
else:
    print("Invalid Choice")