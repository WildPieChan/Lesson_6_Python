# Write a program that accepts a real number
# as input and shows the sum of its digits.

def InputNumber(inputText):
    ok = False
    while not ok:
        try:
            number = float(input(f"{inputText}"))
            ok = True
            if number % 1 > 0:
                number = int(number)
        except ValueError:
            print("Error. Only numbers. Try again...")
    return number

n = InputNumber("Enter any number: ")
result = list(map(int, filter(lambda n: n != '.', str(n))))
print(sum(result))