a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
choice = input("Enter an operator: ")
if choice == "+":
    print(a+b)
elif choice == "-":
    print(a-b)
elif choice == "*":
    print(a*b)
elif choice == "/":
    print(a/b)
elif choice == "%":
    print(a % b)
else:
    print("Enter a valid operator!!")
