def divide_numbers():
    while True:
        try:
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
            num1 = float(num1)
            num2 = float(num2)
            result = num1 / num2
            print(f"The result of {num1} divided by {num2} is: {result}")
            break 
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter a non-zero second number.")

divide_numbers()
