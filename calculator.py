

def calculator():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Choose an operation (1-5): ")

        if choice == "5":
            print("Goodbye! Calculator closed.")
            break

        # Input 
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        # Perform 
        if choice == "1":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == "4":
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print(" Cannot divide by zero.")
        else:
            print(" Invalid choice. Please select from 1 to 5.")

# Run
calculator()
