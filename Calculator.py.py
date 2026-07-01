# CALCULATOR PROJECT

print("Welcome to Calculator Project!")

while True:     # outer loop (to repeat calculator)

    # Operation list
    operations = ["Addition", "Subtraction", "Multiplication", "Division"]
    for i, op in enumerate(operations, start=1):
        print(f"{i}. {op}")
    print("5. Exit")

    # User choice
    choice = int(input("Enter your choice (1-4 for operations, 5 to exit): "))

    # Validate choice
    if choice in [1, 2, 3, 4]:
        print("Valid choice! Continue with calculation...")
    elif choice == 5:
        print("Ending the program, goodbye!")
        break
    else:
        print("Invalid choice! Please enter again.\n")
        continue   # go back to start of loop

    # Take input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform operations
    if choice == 1:
        result = num1 + num2
    elif choice == 2:
        result = num1 - num2
    elif choice == 3:
        result = num1 * num2
    elif choice == 4:
        if num2 == 0:
            print("Division by zero is not allowed!")
            continue
        else:
            result = num1 / num2

    # Display result
    print(f"Result is: {result}")

    # Ask user to continue
    use_again = input("Do you want to continue? (yes/no): ").lower()
    if use_again != "yes":
        print("Program ended. Thanks for using the calculator!")
        break

    print("\nRestarting Calculator\n")
