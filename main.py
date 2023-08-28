class Math:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def substrate(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return int(self.num1 / self.num2)


try:
    num1 = int(input("> "))

    while num1 > 0:
        method = input("Method (+, -, /, *, =, clear): ")

        if method == "+":
            num2 = int(input("(+) > "))

            calculate = Math(num1, num2)
            num1 = calculate.addition()

            print(num1)

        elif method == "-":
            num2 = int(input("(-) > "))

            calculate = Math(num1, num2)
            num1 = calculate.substrate()

            print(num1)

        elif method == "*":
            num2 = int(input("(*) > "))

            calculate = Math(num1, num2)
            num1 = calculate.multiply()

            print(num1)

        elif method == "/":
            num2 = int(input("(/) > "))

            calculate = Math(num1, num2)
            num1 = calculate.divide()

            print(num1)

        elif method == "=":
            print(f"The Value is {num1}")
            break

        elif method.lower() == "clear":
            break

        elif method.lower() == "":
            print("Enter a Method...")

        else:
            print("Invalid Method...")

except ValueError:
    print("Write a valid value.")
