import calculator

num1 = float(input("Enter first no: "))
num2 = float(input("enter second no: "))

operation = input("choose an operation (+, -, *, /) ")

if operation == '+':
    print(f'Result: {calculator.add(num1, num2)}')
elif operation == '-':
    print(f'Result: {calculator.sub(num1, num2)}')
elif operation == '*':
    print(f'Result: {calculator.mul(num1, num2)}')
elif operation == '/':
    print(f'Result: {calculator.div(num1, num2)}')
else:
    print("Invalid operator")