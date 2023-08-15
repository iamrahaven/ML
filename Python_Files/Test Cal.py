class cal():
    def calculator():
        while True:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                c = input("Enter the c (+, -, *, /): ")
            
                if c == '+':
                    result = a + b
                elif c == '-':
                    result = a - b
                elif c == '*':
                    result = a * b
                elif c == '/':
                    if b == 0:
                        print("Error: Division by zero is not allowed!")
                        continue
                    else:
                        result = a / b
                else:
                    print("Invalid c!")
                    continue
            
                print("Result:", result)
        
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
            except KeyboardInterrupt:
                print("\nCalculator terminated.")
                break

    calculator()
