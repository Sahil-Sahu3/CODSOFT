def calculator():
    print("Hello! Welcome to your personal calculator ")
    name = input("What's your name? ")

    print(f"\nNice to meet you, {name}! Let's do some math together.")

    while True:
        print("\n--- Simple Calculator Menu ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ").strip()

        if choice == "5":
            print(f"Goodbye, {name}! Hope to see you again. ")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Hmm... that doesn't look right. Choose a number from 1 to 5.")
            continue

        # Input numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Oops! That wasn't a valid number. Let's try again.")
            continue

        # Perform calculation
        if choice == "1":
            result = num1 + num2
            print(f"You chose to add. Result: {num1} + {num2} = {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"You chose to subtract. Result: {num1} - {num2} = {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"You chose to multiply. Result: {num1} * {num2} = {result}")
        elif choice == "4":
            if num2 == 0:
                print("Uh-oh! You can't divide by zero.")
            else:
                result = num1 / num2
                print(f"You chose to divide. Result: {num1} / {num2} = {result}")

# Start the calculator
calculator()
